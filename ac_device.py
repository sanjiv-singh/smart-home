
import json
import paho.mqtt.client as mqtt
from device import Device


class ACDevice(Device):
    
    _DEVICE_TYPE = "AC"
    _MIN_TEMP = 18  
    _MAX_TEMP = 32  

    def __init__(self, device_id, room):
        
        # Assigning device level information for each of the devices.
        self._temperature = 22
        super().__init__(device_id, room, self._DEVICE_TYPE)

    # Getting the current switch status of devices 
    def _get_switch_status(self):
        pass

    # Setting the the switch of devices
    def _set_switch_status(self, switch_state):
        pass

    # Getting the temperature for the devices
    def _get_temperature(self):
        pass        

    # Setting up the temperature of the devices
    def _set_temperature(self, temperature):
        pass
    
