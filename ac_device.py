
import json
import paho.mqtt.client as mqtt
from device import Device


class ACDevice(Device):
    
    _MIN_TEMP = 18  
    _MAX_TEMP = 32  

    def __init__(self, device_id, room):
        
        self._temperature = 22
        self._device_type = "AC"
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

    # Getting the temperature for the devices
    def _get_temperature(self):
        pass        

    # Setting up the temperature of the devices
    def _set_temperature(self, temperature):
        pass
    
