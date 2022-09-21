import json
import paho.mqtt.client as mqtt
from device import Device



class LightDevice(Device):

    # setting up the intensity choices for Smart Light Bulb  
    _INTENSITY = ["LOW", "HIGH", "MEDIUM", "OFF"]
    _DEVICE_TYPE = "LIGHT"

    def __init__(self, device_id, room):
        # Assigning device level information for each of the devices. 
        self._intensity = "LOW"
        super().__init__(device_id, room, self._DEVICE_TYPE)

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
