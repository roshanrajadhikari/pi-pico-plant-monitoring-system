<h1 align="center" id="title">Pi Pico Plant Monitoring System</h1>

<p align="center"><img src="https://socialify.git.ci/roshanrajadhikari/pi-pico-plant-monitoring-system/image?description=1&amp;font=Inter&amp;forks=1&amp;issues=1&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Circuit%20Board&amp;pulls=1&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

<p id="description">Micropython powred Pi Pico for plant monitoring using MQTT communication.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Soil Moisture Monitoring

<h2>🛠️ Installation Steps:</h2>

<p>1. Prerequisite</p>

```
- Need to have MQTT broker setup
- Follow official documentation to suit your method of install --> https://mosquitto.org/documentation/
```

<p>2. Install VSCode</p>

```
https://code.visualstudio.com/download
```

<p>3. Install MicroPico extension on VSCode</p>

```
Extension ID: paulober.pico-w-go
```

<p>4.Clone This Repo</p>

<p>5.Change client id for Broker class </p>

```
Find the mqtt_client_id variable in Broker and change it to your desire
```
<p>6.Fill Wifi details and mqtt server details in secrets.py file </p>

```
This file holds essential strings necessary for establishing a connection with an MQTT Broker
```


  
<h2>💻 Built with</h2>

Technologies used in the project:

*   MicroPython
*   MQTT
*   Home Assistant
