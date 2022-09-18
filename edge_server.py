
import json
import time
import paho.mqtt.client as mqtt

HOST = "localhost"
PORT = 1883     
WAIT_TIME = 0.25

REQUEST_TOPIC = 'device_request'
MESSAGE_TOPIC = 'device'


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
        self.client.subscribe(REQUEST_TOPIC + '/#')
        
    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload)
        if payload.get('request_type') == 'register':
            del payload["request_type"]
            self._register_device(payload)

    # Returning the current registered list
    def _register_device(self, payload):
        device_id = payload.get('device_id')
        message_topic = MESSAGE_TOPIC + '/?/?/' + device_id
        print(f'Registering device {device_id} on Edge Server.')
        if device_id in [d["device_id"] for d in self._registered_list]:
            print(f'Device {device_id} already registered.')
            message = {"msg_type": "ERROR", "msg": "Device already registered"}
        else:
            self._registered_list.append(payload)
            message = {"msg_type": "INFO", "msg": f"Device {device_id} succesfully registered"}
        self.client.publish(message_topic, json.dumps(message))

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
