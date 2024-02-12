from machine import Pin
import utime
import _thread
import uasyncio as asyncio
from aswitch import Pushbutton
from util.filesys import FileIO
from broker import Broker
from menu.menu import Menu #import the Menu class
from sensor.sensor import Sensor
#from sensor.sensorlist import sensor_list

fileio = FileIO() # FileIO instance

# Set the GPIO pin  for button input
button = Pin(14,Pin.IN,Pin.PULL_DOWN)

pb = Pushbutton(button,suppress=True)

sensor_list = fileio.read("data/sensorlist.dat")  # Read the sensor list from file
# Create a list of Sensor instances using a list comprehension
sensors = [Sensor(sensor["pin"], sensor["min_in"], sensor["max_in"], sensor["name"]) for sensor in sensor_list]

broker = Broker(sensors) # service broker instance
menu = Menu(broker)
keep_alive = True

bg_task_active = False

#2nd core background task
def background_task():
    global bg_task_active, keep_alive
    bg_task_active = True
    
    pb.long_func(menu.handle_button_press,("long",))

    pb.release_func(menu.handle_button_press,("single",))
    
    try:
        loop = asyncio.get_event_loop()
        print("starting menu")
        loop.run_until_complete(menu.start())
    except BaseException as e:
        print(f"Error in background_task: {e}")
        # Handle specific exceptions if needed
    finally:
        bg_task_active = False
        #keep_alive = False
        menu.is_running = False
        print("menu off")
       
def start_bg_task():
    _thread.start_new_thread(background_task, ())  #start background thread

def core():     
    global keep_alive, menu
    
    try:
        while keep_alive:
            
            broker.publish() # publish data to mqtt
            utime.sleep_ms(2000)  # wait 2 seconds
    except BaseException as e:
        print(f"Error in core0: {e}")
        # Handle specific exceptions if needed
    finally:
        keep_alive = False
        menu.is_running = False
        print("program was closed")

def button_handler(irq):
    global bg_task_active, keep_alive
    try:
        if not bg_task_active and keep_alive :
            start_bg_task()
    except BaseException as e:
        print(f"Error in button_handler: {e}")
        
try:
    button.irq(trigger=Pin.IRQ_RISING, handler=button_handler ) #set button interrupt handler
    print("core")
    core() # Start the core function using asyncio.run
except BaseException as e:
    print(f"Error in main program: {e}")
    
finally:
    keep_alive = False
    menu.is_running = False
    pass
