from broker import Broker
from sensor import Sensor
import time

sensor = Sensor(28,50000,23000) #sensor instance params: ADC pin, value when no moisture, value when max moisture
broker = Broker() # service broker instance



while True:
    broker.publish(sensor) #publish data to mqtt
    time.sleep(1) #wait a second

