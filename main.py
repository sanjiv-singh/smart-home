import time
from edge_server import EdgeServer
from light_device import LightDevice
from ac_device import ACDevice

WAIT_TIME = 0.25  

print("\nSmart Home Simulation started.")
# Creating the edge-server for the communication with the user

edge_server_1 = EdgeServer('edge_server_1')
time.sleep(WAIT_TIME)  

print("Intitate the device creation and registration process." )

print('\n******************* REGSITRATION OF THE DEVICES THROUGH SERVER *******************')

# Creating the light_device
print("\nCreating and registering Light devices for their respective rooms.")

print('\n******************* REGSITRATION OF LIGHT DEVICES INITIATED *******************')
light_device_1 = LightDevice("light_1", "Kitchen")
time.sleep(WAIT_TIME)  

light_device_2 = LightDevice("light_2", "LR")
time.sleep(WAIT_TIME)  

light_device_3 = LightDevice("light_3", "LR")
time.sleep(WAIT_TIME)  

light_device_4 = LightDevice("light_4", "BR1")
time.sleep(WAIT_TIME)  

light_device_5 = LightDevice("light_5", "BR2")
time.sleep(WAIT_TIME)  

# Creating the ac_device  
print("\nCreating the AC devices for their respective rooms. ")

print('\n******************* REGSITRATION OF AC DEVICES INITIATED *******************')
ac_device_1 = ACDevice("ac_1", "BR1")
time.sleep(WAIT_TIME)  

ac_device_2 = ACDevice("ac_2", "BR2")
time.sleep(WAIT_TIME)  

ac_device_3 = ACDevice("ac_3", "LR")
time.sleep(WAIT_TIME)  

ac_device_4 = ACDevice("ac_4", "LR")
time.sleep(WAIT_TIME)  

print('******************* REGSITRED DEVICES ON THE SERVER *******************a')

print('Fetching the list of registered devices from EdgeServer')
registered_devices = edge_server_1.get_registered_device_list()
print('The Registered devices on Edge-Server:')
print([device["device_id"] for device in registered_devices])

print('\n******************* GETTING THE STATUS AND CONTROLLING THE DEVICES *******************')

print('\nGetting the status of all devices')
edge_server_1.get_status()
time.sleep(WAIT_TIME)

print('\nGetting the status of devices by room_type = BR1')
edge_server_1.get_status("room_type", "BR1")
time.sleep(WAIT_TIME)

print('\nGetting the status of devices by device_type = AC')
edge_server_1.get_status("device_type", "AC")
time.sleep(WAIT_TIME)

print('\nGetting the status of devices by device_id = light_2')
edge_server_1.get_status("device_id", "light_2")
time.sleep(WAIT_TIME)

print('\n******************* SETTING THE STATUS OF DEVICE *******************')
print('\nSetting the switch state of devices by device_id = light_2')
edge_server_1.set("device_id", "light_2", "switch", "ON")
time.sleep(WAIT_TIME)

print('Getting the switch state of device light_2 for verifying')
edge_server_1.get_status("device_id", "light_2")
time.sleep(WAIT_TIME)

print('\nSetting the switch state of devices by device_type = LIGHT')
edge_server_1.set("device_type", "LIGHT", "switch", "ON")
time.sleep(WAIT_TIME)

print('Getting the switch state of light devices for verifying')
edge_server_1.get_status("device_type", "LIGHT")
time.sleep(WAIT_TIME)

print('\nSetting the switch state of devices by room_type = LR')
edge_server_1.set("room_type", "LR", "switch", "OK")
time.sleep(WAIT_TIME)

print('Getting the switch state of devices in Living Room for verifying')
edge_server_1.get_status("room_type", "LR")
time.sleep(WAIT_TIME)

print('\nSetting the switch state of all devices')
edge_server_1.set("all", None, "switch", "ON")
time.sleep(WAIT_TIME)

print('Getting the switch state of all devices')
edge_server_1.get_status("all", None)
time.sleep(WAIT_TIME)

print('\nSetting the intensity of device_id light_3')
edge_server_1.set("device_id", "light_3", "intensity", "MIN")
time.sleep(WAIT_TIME)

print('\nSetting the intensity of device_id light_3')
edge_server_1.set("device_id", "light_3", "intensity", "MEDIUM")
time.sleep(WAIT_TIME)

print('Getting the intensity of device light_3 for verifying')
edge_server_1.get_status("device_id", "light_3")
time.sleep(WAIT_TIME)

print('\nSetting the temperature of device_id ac_3')
edge_server_1.set("device_id", "ac_3", "temperature", "12")
time.sleep(WAIT_TIME)

print('\nSetting the temperature of device_id ac_3')
edge_server_1.set("device_id", "ac_3", "temperature", "22")
time.sleep(WAIT_TIME)

print('Getting the temperature of device ac_3 for verifying')
edge_server_1.get_status("device_id", "ac_3")
time.sleep(WAIT_TIME)


print("\nSmart Home Simulation stopped.")
light_device_1.terminate()
ac_device_1.terminate()
edge_server_1.terminate()
