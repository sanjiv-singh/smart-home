
import json
import time
import paho.mqtt.client as mqtt

HOST = "localhost"
PORT = 1883     
WAIT_TIME = 0.25  

class EdgeServer:
    
    def __init__(self, instance_name):
        
        self._instance_id = instance_name
        self.client = mqtt.Client(self._instance_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(HOST, PORT, keepalive=60)
        self.client.loop_start()
        self._registered_list = []

    # Terminating the MQTT broker and stopping the execution
    def terminate(self):
        self.client.disconnect()
        self.client.loop_stop()

    # Connect method to subscribe to various topics.     
    def _on_connect(self, client, userdata, flags, result_code):
        self.client.subscribe('device_request/#')
        
    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload)
        if payload.get('request_type') == 'register':
            self._register_device(payload.get("device_id"))

    # Returning the current registered list
    def _register_device(self, device_id):
        print(f'Registering device {device_id} on Edge Server.')
        if device_id in self._registered_list:
            print(f'Device {device_id} already registered.')
            return
        self._registered_list.append(device_id)

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
