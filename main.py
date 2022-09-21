import time
from edge_server import EdgeServer
from light_device import LightDevice
from ac_device import ACDevice

WAIT_TIME = 0.25  

print("\nSmart Home Simulation started.")
# Creating the edge-server for the communication with the user

edge_server_1 = EdgeServer('edge_server_1')
time.sleep(WAIT_TIME)  

# Creating the light_device
print("Intitate the device creation and registration process." )
print("\nCreating the Light devices for their respective rooms.")
light_device_1 = LightDevice("light_1", "Kitchen")
time.sleep(WAIT_TIME)  

# Creating the ac_device  
print("\nCreating the AC devices for their respective rooms. ")
ac_device_1 = ACDevice("ac_1", "BR1")
time.sleep(WAIT_TIME)  

print("\nSmart Home Simulation stopped.")
light_device_1.terminate()
ac_device_1.terminate()
edge_server_1.terminate()
