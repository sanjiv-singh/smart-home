from abc import ABC, abstractmethod
import json
import paho.mqtt.client as mqtt


HOST = "localhost"
PORT = 1883
    
class Device(ABC):
    
    def __init__(self, device_id, room, device_type):
        
        self._device_id = device_id
        self._room_type = room
        self._device_type = device_type
        self._device_registration_flag = False
        self._inbound_topic = f'inbound/{room}/{device_type}/{device_id}'
        self._outbound_topic = f'outbound/{device_id}'
        self.client = mqtt.Client(self._device_id)  
        self.client.on_connect = self._on_connect  
        self.client.on_message = self._on_message  
        self.client.on_disconnect = self._on_disconnect  
        self.client.connect(HOST, PORT, keepalive=60)  
        self.client.loop_start()  
        self._switch_status = "OFF"
        self._register_device(self._device_id, self._room_type, device_type)
        self._device_registration_flag = True

    # calling registration method to register the device
    def _register_device(self, device_id, room_type, device_type):
        message = {
                "device_id": device_id,
                "request_type": "register",
                "room_type": room_type,
                "device_type": device_type
        }
        self.client.publish(self._outbound_topic, json.dumps(message))

    # Connect method to subscribe to various topics. 
    @abstractmethod
    def _on_connect(self, client, userdata, flags, result_code):
        self.client.subscribe(self._inbound_topic)

    # Disconnect method to terminate connection. 
    @abstractmethod
    def _on_disconnect(self, client, userdata, result_code):
        pass

    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg): 
        print("Received msg...")
        print(msg.payload)

    # Getting the current switch status of devices 
    @abstractmethod
    def _get_switch_status(self):
        pass

    # Setting the the switch of devices
    @abstractmethod
    def _set_switch_status(self, switch_state):
        pass

