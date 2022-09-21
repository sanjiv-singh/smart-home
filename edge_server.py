import json
import time
import paho.mqtt.client as mqtt

HOST = "localhost"
PORT = 1883     
WAIT_TIME = 0.25

OUTBOUND_TOPIC = 'outbound'
INBOUND_TOPIC = 'inbound'


class EdgeServer:

    def __init__(self, instance_name):
        
        self._instance_id = instance_name
        self.client = mqtt.Client(self._instance_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(HOST, PORT, keepalive=60)
        self.client.loop_start()
        self._registered_list = []
        self._MESSAGE_ACTION_MAPPING = {
            "REGISTER": self._register_device,
            "ERROR": self._report_error,
            "INFO": self._log,
            "ACK": self._log
        }
    

    # Terminating the MQTT broker and stopping the execution
    def terminate(self):
        self.client.disconnect()
        self.client.loop_stop()

    # Connect method to subscribe to various topics.     
    def _on_connect(self, client, userdata, flags, result_code):
        self.client.subscribe(OUTBOUND_TOPIC + '/#')
        
    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload)
        msg_type = payload.get("msg_type")
        action = self._MESSAGE_ACTION_MAPPING[msg_type]
        action(payload)

    # Returning the current registered list
    def _register_device(self, payload):
        device_id = payload.get('device_id')
        room_type = payload.get('room_type')
        inbound_topic = f'{INBOUND_TOPIC}/{payload.get("room_type")}/{payload.get("device_type")}/{device_id}'
        print(f'Edge: Registering device {device_id} for {room_type}')
        if device_id in [d["device_id"] for d in self._registered_list]:
            print(f'Edge: Device {device_id} already registered.')
            message = {"msg_type": "ERROR", "msg": "Device already registered"}
        else:
            self._registered_list.append(payload)
            message = {"msg_type": "INFO", "msg": f"Device {device_id} succesfully registered for {room_type}"}
        self.client.publish(inbound_topic, json.dumps(message), qos=2)

    # Returning the current registered list
    def get_registered_device_list(self):
        return self._registered_list

    # Getting the status for the connected devices
    def get_status(self):
        pass

    # Controlling and performing the operations on the devices
    # based on the request received
    def set(self):
        pass

    def _report_error(self, payload):
        self._raise_alert(payload)
        self._log(payload)

    def _log(self, payload):
        print(f'Edge: Received {payload}')

    def _raise_alert(self, payload):
        pass

