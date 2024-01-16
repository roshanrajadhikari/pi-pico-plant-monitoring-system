import utime
import _thread
from broker import Broker
from sensor import Sensor
from menu.menu import Menu #import the Menu class
from sensorlist import sensor_list

# Create a list of Sensor instances using a list comprehension
sensors = [Sensor(sensor["pin"], sensor["min_in"], sensor["max_in"], sensor["name"]) for sensor in sensor_list]

broker = Broker(sensors) # service broker instance
menu = Menu(broker)
keep_alive = True

#2nd core background task
def core1_task():
    #run background thread for reading sensors and sending it to mqqt server
    while keep_alive:
        broker.publish() #publish data to mqtt
        utime.sleep(2) #wait a second

_thread.start_new_thread(core1_task, ())  #start background thread

try:
    #main core
    menu.start()
except BaseException as e: #if there was bad exit
    #Bad exit: anything that will cause interruption and exit program without user's "exit" input
    print(e)
    pass

print("System halted. Shutting down")
keep_alive = False #safely flag down
    
    





