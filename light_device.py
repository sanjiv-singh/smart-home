import json
import paho.mqtt.client as mqtt
from device import Device



class LightDevice(Device):

    # setting up the intensity choices for Smart Light Bulb  
    _INTENSITY = ["LOW", "HIGH", "MEDIUM", "OFF"]

    def __init__(self, device_id, room):
        # Assigning device level information for each of the devices. 
        self._device_type = "LIGHT"
        super().__init__(device_id, room)

    # Connect method to subscribe to various topics. 
    def _on_connect(self, client, userdata, flags, result_code):
        pass

    # Disconnect method to terminate connection. 
    def _on_disconnect(self, client, userdata, result_code):
        pass

    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        pass

    # Getting the current switch status of devices 
    def _get_switch_status(self):
        pass

    # Setting the the switch of devices
    def _set_switch_status(self, switch_state):
        pass

    # Getting the light intensity for the devices
    def _get_light_intensity(self):
        pass

    # Setting the light intensity for devices
    def _set_light_intensity(self, light_intensity):
        pass    
