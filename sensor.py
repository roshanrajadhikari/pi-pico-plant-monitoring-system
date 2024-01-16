from machine import ADC

class Sensor:

    #init the class first 
    def __init__(self,pin,min,max,name):
        self.pin = pin 
        self.min = min
        self.max = max
        self.sensor = ADC(pin) #setting sensor ADC pin
        self.name = name
        self.topic = 'sensor/sensor' + str(pin)
    
        
    def readData(self):
        return self.sensor.read_u16() #raw data is returned after reading the raw value from the sensorwhich is mapped and filtered using broker 

