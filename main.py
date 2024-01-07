from broker import Broker
from sensor import Sensor
import time

sensor = Sensor(28,50000,23000) #sensor instance params: ADC pin, value when no moisture, value when max moisture
broker = Broker() # service broker instance
topic = "dev" #topic to publish data in mqtt

while True:
    data = str(sensor.readData()) #reading value from sensor
    broker.publish(data, topic) #publish data to mqtt
    time.sleep(1) #wait a second


