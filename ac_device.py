
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
        self._MESSAGE_ACTION_MAPPING["SET_SWITCH"] = self._set_switch_status
        self._MESSAGE_ACTION_MAPPING["SET_TEMPERATURE"] = self._set_temperature

    # Getting the current switch status of AC devices
    def _get_status(self, payload=None):
        payload = {"msg_type": "STATUS",
                "device_id": self._device_id,
                "room_type": self._room_type,
                "device_type": self._device_type,
                "switch_state": self._switch_status,
                "temperature": self._temperature}
        self.client.publish(self._outbound_topic, json.dumps(payload), qos=2)

    
    # Getting the light intensity for the devices
    def _get_switch_status(self):
        return self._switch_status

    # Setting the the switch of devices
    def _set_switch_status(self, payload):
        status = payload.get("value")
        if status in ["ON", "OFF"]:
            self._switch_status = payload.get("value")
            return_payload = {"msg_type": "INFO", "msg": f"Succesfully changed status of {self._device_id} to {status}"}
        else:
            return_payload = {"msg_type": "ERROR", "msg": f"{status}: Not a valid switch status"}
        self.client.publish(self._outbound_topic, json.dumps(return_payload))

    # Getting the temperature for the devices
    def _get_temperature(self):
        return self._temperature        

    # Setting up the temperature of the devices
    def _set_temperature(self, payload):
        temperature = payload.get("value")
        if int(temperature) >= self._MIN_TEMP and int(temperature) <= self._MAX_TEMP:
            self._temperature = temperature
            return_payload = {"msg_type": "INFO", "msg": f"Succesfully changed temperature of {self._device_id} to {temperature}"}
        else:
            return_payload = {"msg_type": "ERROR", "msg": f"{temperature}: Not a valid temperature value"}
        self.client.publish(self._outbound_topic, json.dumps(return_payload))

