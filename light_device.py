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
        self._MESSAGE_ACTION_MAPPING["SET_SWITCH"] = self._set_switch_status
        self._MESSAGE_ACTION_MAPPING["SET_INTENSITY"] = self._set_light_intensity

    # Getting the current switch status of light devices
    def _get_status(self, payload=None):
        payload = {"msg_type": "STATUS",
                "device_id": self._device_id,
                "room_type": self._room_type,
                "device_type": self._device_type,
                "switch_state": self._switch_status,
                "intensity": self._intensity}
        self.client.publish(self._outbound_topic, json.dumps(payload), qos=2)

    # Getting the light intensity for the devices
    def _get_switch_status(self):
        pass

    # Setting the the switch of devices
    def _set_switch_status(self, payload):
        status = payload.get("value")
        if status in ["ON", "OFF"]:
            self._switch_status = status
            return_payload = {"msg_type": "INFO", "msg": f"Succesfully changed status of {self._device_id} to {status}"}
        else:
            return_payload = {"msg_type": "ERROR", "msg": f"{status}: Not a valid switch status"}
        self.client.publish(self._outbound_topic, json.dumps(return_payload))

    # Getting the light intensity for the devices
    def _get_light_intensity(self):
        return self._intensity

    # Setting the light intensity for devices
    def _set_light_intensity(self, payload):
        intensity = payload.get("value")
        if intensity in self._INTENSITY:
            self._intensity = intensity
            return_payload = {"msg_type": "INFO", "msg": f"Succesfully changed intensity of {self._device_id} to {intensity}"}
        else:
            return_payload = {"msg_type": "ERROR", "msg": f"{intensity}: Not a valid intensity value"}
        self.client.publish(self._outbound_topic, json.dumps(return_payload))
