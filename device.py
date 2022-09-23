from abc import ABC, abstractmethod
import json
import paho.mqtt.client as mqtt


HOST = "localhost"
PORT = 1883
OUTBOUND_TOPIC = 'outbound'
INBOUND_TOPIC = 'inbound'

    
class Device(ABC):
    
    def __init__(self, device_id, room, device_type):
        
        self._MESSAGE_ACTION_MAPPING = {
            "GET_STATUS": self._get_status,
            "ERROR": self._report_error,
            "INFO": self._ack,
            "ACK": self._log
        }

        self._device_id = device_id
        self._room_type = room
        self._device_type = device_type
        self._device_registration_flag = False
        self._switch_status = "OFF"
        self._inbound_topic = f'{INBOUND_TOPIC}/{room}/{device_type}/{device_id}'
        self._outbound_topic = f'{OUTBOUND_TOPIC}/{device_id}'
        self.client = mqtt.Client(self._device_id)  
        self.client.on_connect = self._on_connect  
        self.client.on_message = self._on_message  
        self.client.connect(HOST, PORT, keepalive=60)  
        self.client.loop_start()  
        self._register_device(self._device_id, self._room_type, device_type)
        self._device_registration_flag = True

    # calling registration method to register the device
    def _register_device(self, device_id, room_type, device_type):
        message = {
                "device_id": device_id,
                "msg_type": "REGISTER",
                "room_type": room_type,
                "device_type": device_type
        }
        self.client.publish(self._outbound_topic, json.dumps(message), qos=2)

    # Connect method to subscribe to various topics. 
    def _on_connect(self, client, userdata, flags, result_code):
        self.client.subscribe(self._inbound_topic)

    # Terminate method to terminate connection. 
    def terminate(self):
        self.client.disconnect()
        self.client.loop_stop()  

    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg): 
        payload = json.loads(msg.payload)
        msg_type = payload.get("msg_type")
        action = self._MESSAGE_ACTION_MAPPING[msg_type]
        action(payload)

    # Getting the current switch status of devices 
    def _get_status(self, payload=None):
        payload = {"msg_type": "STATUS",
                "device_id": self._device_id,
                "room_type": self._room_type,
                "device_type": self._device_type,
                "switch_state": self._switch_state,
                "intensity": self._intensity}
        self.client.publish(self._outbound_topic, json.dumps(payload), qos=2)

    # Setting the the switch of devices
    @abstractmethod
    def _set_switch_status(self, switch_state):
        pass

    def _ack(self, payload):
        self._log(payload)
        ack_payload = {
            "msg_type": "ACK",
            "msg": payload.get("msg")
        }
        self.client.publish(self._outbound_topic, json.dumps(ack_payload), qos=2)

    def _report_error(self, payload):
        self._raise_alert(payload)
        self._log(payload)

    def _log(self, payload):
        print(f'Device {self._device_id}: Received {payload}')

    def _raise_alert(self, payload):
        pass

