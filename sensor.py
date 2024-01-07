from machine import ADC

class Sensor:

    #init the class first 
    def __init__(self,pin,min,max):
        self.pin = pin 
        self.min = min
        self.max = max
        self.sensor = ADC(pin)
    
    # A handy function for mapping values
    def __map_range(self,x, in_min_val, in_max_val, out_min, out_max):
        mapped = (x - in_min_val) * (out_max - out_min) / (in_max_val - in_min_val) + out_min
        return int(max(min(mapped, out_max), out_min))

    def readData(self):
        raw_data_reading = self.sensor.read_u16()
        filtered_data = self.__map_range(raw_data_reading, self.min, self.max, 0, 100)
        return filtered_data
