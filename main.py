import utime
import _thread
from broker import Broker
from sensor import Sensor
from menu.menu import Menu #import the Menu class


sensors = [Sensor(28,50000,23000),Sensor(27,50000,23000)] #sensor instance params: ADC pin, value when no moisture, value when max moisture
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
    
    





