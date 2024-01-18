import utime
import _thread
from broker import Broker
from sensor import Sensor
from menu.menu import Menu #import the Menu class
from sensorlist import sensor_list

from machine import Pin

# Set the GPIO pin  for button input
touch_pin = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Create a list of Sensor instances using a list comprehension
sensors = [Sensor(sensor["pin"], sensor["min_in"], sensor["max_in"], sensor["name"]) for sensor in sensor_list]

broker = Broker(sensors) # service broker instance
menu = Menu(broker)
keep_alive = True

#2nd core background task
def background_task():
    #run background thread for UI and user interaction with the system
    menu.start()
    
def start_bg_task():
    _thread.start_new_thread(background_task, ())  #start background thread
    
try:
    #main core
    while keep_alive:
        #when menu is not running and user has pressed the button 
        #start the menu in background thread
        if(not menu.is_running and touch_pin.value()):
            #start the menu
            start_bg_task()
            
        broker.publish() #publish data to mqtt
        utime.sleep(2) #wait a second
except BaseException as e: #if there was bad exit
    #Bad exit: anything that will cause interruption and exit program without user's "exit" input
    print(e)
    pass


#this runs when main core is failed
print("System halted. Shutting down")
keep_alive = False #stop the main core loop
menu.is_running = False #safely exit the menu
   
    





