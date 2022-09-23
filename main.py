import time
from edge_server import EdgeServer
from light_device import LightDevice
from ac_device import ACDevice

WAIT_TIME = 0.25  

print("\nSmart Home Simulation started.")
# Creating the edge-server for the communication with the user

edge_server_1 = EdgeServer('edge_server_1')
time.sleep(WAIT_TIME)  

print("\n=========================== REQUIREMENT 1 (DEVICE REGISTRATION) ===========================")

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

print('\nFetching the list of registered devices from EdgeServer')
registered_devices = edge_server_1.get_registered_device_list()
print('The Registered devices on Edge-Server:')
print([device["device_id"] for device in registered_devices])

print('Testing of Requirement 1 completed.')

print("\n=========================== REQUIREMENT 2 (DEVICE STATUS & SWITCH ON/OFF) ===========================")

print('\n************************* GETTING DEVICE STATUS (REQMT 2A) *************************')

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

print('\n******************* SETTING SWITCH STATUS ON DEVICE (REQMT 2B) *******************')
print('\nSetting the switch state of devices by device_id = light_2')
edge_server_1.set("device_id", "light_2", "switch", "ON")
time.sleep(WAIT_TIME)

print('Getting the switch state of device light_2 for verification')
edge_server_1.get_status("device_id", "light_2")
time.sleep(WAIT_TIME)

print('\nSetting the switch state of devices by device_type = LIGHT with invalid value (Should Fail)')
edge_server_1.set("device_type", "LIGHT", "switch", "XX")
time.sleep(WAIT_TIME)

print('\nSetting the switch state of devices by device_type = AC')
edge_server_1.set("device_type", "AC", "switch", "ON")
time.sleep(WAIT_TIME)

print('Getting the switch state of AC devices for verification')
edge_server_1.get_status("device_type", "AC")
time.sleep(WAIT_TIME)

print('\nSetting the switch state of devices by room_type = LR with invalid value (Should fail)')
edge_server_1.set("room_type", "LR", "switch", "OK")
time.sleep(WAIT_TIME)

print('\nSetting the switch state of devices by room_type = LR')
edge_server_1.set("room_type", "LR", "switch", "ON")
time.sleep(WAIT_TIME)

print('Getting the switch state of devices in Living Room for verification')
edge_server_1.get_status("room_type", "LR")
time.sleep(WAIT_TIME)

print('\nSetting the switch state of all devices')
edge_server_1.set("all", None, "switch", "ON")
time.sleep(WAIT_TIME)

print('Getting the switch state of all devices for verification')
edge_server_1.get_status("all", None)
time.sleep(WAIT_TIME)

print('Testing of Requirement 2 completed.')

print("\n==================== REQUIREMENT 3 (DEVICE CONTROL COMMANDS) ====================")

print('\n************************* LIGHT INTENSITY CONTROL (REQMT 3A) *************************')

print('\nSetting the intensity of device_id light_3 with invalid intensity value (Should Fail)')
edge_server_1.set("device_id", "light_3", "intensity", "MIN")
time.sleep(WAIT_TIME)

print('\nSetting the intensity of device_id light_3')
edge_server_1.set("device_id", "light_3", "intensity", "MEDIUM")
time.sleep(WAIT_TIME)

print('Getting the intensity of device light_3 for verification')
edge_server_1.get_status("device_id", "light_3")
time.sleep(WAIT_TIME)

print('\nSetting the intensity of lights in BR1 with invalid intensity value (Should Fail)')
edge_server_1.set("room_type", "BR1", "intensity", "BRIGHT")
time.sleep(WAIT_TIME)

print('\nSetting the intensity of lights in BR1')
edge_server_1.set("room_type", "BR1", "intensity", "HIGH")
time.sleep(WAIT_TIME)

print('Getting the status of devices in BR1 for verification')
edge_server_1.get_status("room_type", "BR1")
time.sleep(WAIT_TIME)

print('\nSetting the intensity of all lights with invalid temperature value (Should Fail)')
edge_server_1.set("device_type", "LIGHT", "temperature", "DIM")
time.sleep(WAIT_TIME)

print('\nSetting the intensity of all lights')
edge_server_1.set("device_type", "LIGHT", "intensity", "MEDIUM")
time.sleep(WAIT_TIME)

print('Getting the status of all lights for verification')
edge_server_1.get_status("device_type", "LIGHT")
time.sleep(WAIT_TIME)

print('\n************************* AC TEMPERATURE CONTROL (REQMT 3B) *************************')

print('\nSetting the temperature of device_id ac_3 with invalid temperature value (Should Fail)')
edge_server_1.set("device_id", "ac_3", "temperature", "12")
time.sleep(WAIT_TIME)

print('\nSetting the temperature of device_id ac_3')
edge_server_1.set("device_id", "ac_3", "temperature", "22")
time.sleep(WAIT_TIME)

print('Getting the temperature of device ac_3 for verification')
edge_server_1.get_status("device_id", "ac_3")
time.sleep(WAIT_TIME)

print('\nSetting the temperature of ACs in BR2 with invalid temperature value (Should Fail)')
edge_server_1.set("room_type", "BR2", "temperature", "12")
time.sleep(WAIT_TIME)

print('\nSetting the temperature of ACs in BR2')
edge_server_1.set("room_type", "BR2", "temperature", "21")
time.sleep(WAIT_TIME)

print('Getting the status of devices in BR2 for verification')
edge_server_1.get_status("room_type", "BR2")
time.sleep(WAIT_TIME)

print('\nSetting the temperature of all ACs with invalid temperature value (Should Fail)')
edge_server_1.set("device_type", "AC", "temperature", "33")
time.sleep(WAIT_TIME)

print('\nSetting the temperature of all ACs')
edge_server_1.set("device_type", "AC", "temperature", "20")
time.sleep(WAIT_TIME)

print('Getting the status of all ACs for verification')
edge_server_1.get_status("device_type", "AC")
time.sleep(WAIT_TIME)


print("\nSmart Home Simulation stopped.")
light_device_1.terminate()
ac_device_1.terminate()
edge_server_1.terminate()
