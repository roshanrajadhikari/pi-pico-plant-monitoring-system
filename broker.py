import network
import time
import secrets
from umqtt.simple import MQTTClient

class Broker:
    def __init__(self):

        #wireless network details
        self.wifi_ssid = secrets.WIFI_SSID
        self.wifi_password = secrets.WIFI_PASSWORD

        #mqtt server details
        self.mqtt_client_id = "devmode" #client id
        self.mqtt_host = secrets.MQTT_HOST #mqtt server host
        self.mqtt_username = secrets.MQTT_USERNAME  # username
        self.mqtt_password = secrets.MQTT_PASSWORD  # pass
        
        self.__initNet()
        self.client = self.__initClient()
        
    
    def __initNet(self):
        #Establish wireless connection to wifi
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.wifi_ssid, self.wifi_password)
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            time.sleep(1)
        print("Connected to WiFi")
    
    def __initClient(self):
        # Initialize our MQTTClient and connect to the MQTT server
        mqtt_client = MQTTClient(
            client_id=self.mqtt_client_id,
            server=self.mqtt_host,
            user=self.mqtt_username,
            password=self.mqtt_password)
        mqtt_client.connect()
        return mqtt_client 
    
    def publish(self,data,topic):
        self.client.publish(topic, data)
        print(f'Data published: {data}')

        