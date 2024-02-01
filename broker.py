import utime
import network
import secrets
from umqtt.simple import MQTTClient

class Broker:
    def __init__(self,sensors):

        #wireless network details
        self.wifi_ssid = secrets.WIFI_SSID
        self.wifi_password = secrets.WIFI_PASSWORD

        #mqtt server details
        self.mqtt_client_id = "devmode" #client id
        self.mqtt_host = secrets.MQTT_HOST #mqtt server host
        self.mqtt_username = secrets.MQTT_USERNAME  # username
        self.mqtt_password = secrets.MQTT_PASSWORD  # pass
        
        self.sensors = sensors
        
        self.__initNet()
        self.client = self.__initClient()
        
    
    def __initNet(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        try:
            #Establish wireless connection to wifi
            wlan.connect(self.wifi_ssid, self.wifi_password)
            while not wlan.isconnected():
                print('Waiting for connection...')
                utime.sleep(1)
            print("Connected to WiFi")
        except Exception as e:
            print(f"Error: {e}")

    
    def __initClient(self):
        # Initialize our MQTTClient and connect to the MQTT server
        mqtt_client = MQTTClient(
            client_id=self.mqtt_client_id,
            server=self.mqtt_host,
            user=self.mqtt_username,
            password=self.mqtt_password)
        mqtt_client.connect()
        return mqtt_client 
    
    # A handy function for mapping raw values taken from the sensor 
    def __map_range(self,sensor_value, in_min_val, in_max_val, out_min, out_max):
        sensor_value = max(in_max_val, min(sensor_value, in_min_val)) #value limiter within minimum and maximum given value
        normal_value = (sensor_value - in_min_val)/(in_max_val- in_min_val) #calculate the normalized value
        mapped_value = out_min + normal_value*(out_max - out_min)  #map to desired range
        return mapped_value

    #function to handle data reading from the sensor
    def sense(self,sensor):
            raw_data = sensor.readData()
            data = int(self.__map_range(raw_data, sensor.min, sensor.max, 0, 100))
            return data
    
    # Function that publishes sensor data
    def publish(self, sensor=None):
        if sensor is None:
            # Publish all sensors
            for sensor in self.sensors:
                topic = sensor.topic
                self.client.publish(topic, str(self.sense(sensor)))
                utime.sleep(0.5)  # Delay reading
        else:
            # Publish data from a specific sensor
            topic = sensor.topic
            self.client.publish(topic, str(self.sense(sensor)))
    
    # for all the sensors read the values and return array    
    def getSensors(self):
        data = []
        for sensor in self.sensors:
            try:
                data.append({"name":sensor.name,"value":self.sense(sensor)})
                #data.append({"name":"test","value":"12"})
            except Exception as e:
                print(f"Error reading sensor {sensor}: {e}")
                # Handle the error, possibly by appending a default value or skipping the sensor
        return data
        