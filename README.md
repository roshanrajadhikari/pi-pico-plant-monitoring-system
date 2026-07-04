<h1 align="center" id="title">Pi Pico Plant Monitoring System</h1>

<p align="center"><img src="https://socialify.git.ci/roshanrajadhikari/pi-pico-plant-monitoring-system/image?description=1&amp;font=Inter&amp;forks=1&amp;issues=1&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Circuit%20Board&amp;pulls=1&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

<p id="description">Micropython powred Pi Pico for plant monitoring using MQTT communication.</p>

## IoT Plant Monitoring System

An automated, multi-threaded IoT telemetry system designed to monitor and report soil moisture, temperature, and environmental conditions in real time using edge hardware.

## 🚀 Key Features
* **Asynchronous Telemetry:** Built with multi-threaded script logic to handle simultaneous sensor scanning and network communication without blocking execution.
* **Lightweight Transport:** Utilizes the MQTT protocol to stream lightweight JSON payloads to a centralized broker.
* **Resilient Networking:** Implemented auto-reconnect fallback logic for stable Wi-Fi connectivity at the edge.

## 🛠️ Tech Stack & Hardware
* **Languages:** MicroPython / Python
* **Hardware Target:** Raspberry Pi Pico W / ESP32
* **Protocols:** MQTT, I2C, Wi-Fi 802.11 b/g/n
* **Sensors:** Capacitive Soil Moisture Sensors

## 📁 Repository Structure
```text
├── data/
│   └── sensorlist.dat # Contains list of sensors and hardware pin connections
├── lib/               # Required lib for project
├── menu/
│   ├── menu.py        # Menu class that handels displaying menu screen and data screen
│   └── menulist.py    # Contains object defining the flow and structure of menu             
├── sensor/
│   └── sensors.py     # Hardware abstraction layers for connected modules
├── aswitch.py         # Lib for button press interruption
├── broker.py          # Broker connection handles and message publishing
├── main.py            # Entry program, setups up interruption handelling, and state management
├── secrets.py         # Contains credentials for wifi and mqtt server
└── README.md
```

## ⚙️ Quick Start & Installation

**Clone the repository:** 
```
git clone [https://github.com/roshanrajadhikari/pi-pico-plant-monitoring-system.git](https://github.com/roshanrajadhikari/pi-pico-plant-monitoring-system.git)
cd pi-pico-plant-monitoring-system
```
**Configure your environment:**
Edit `secrets.py` and populate wifi credentials and mqtt server details.
```
{
  "WIFI_SSID": "Your_Network",
  "WIFI_PASS": "Your_Password",
  "MQTT_BROKER": "192.168.1.50"
}
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Summary of the MIT License:
* **Permissions:** Commercial use, modification, distribution, and private use.
* **Limitations:** The software is provided "as is", without warranty of any kind. 
* **Conditions:** The original copyright notice and permission notice must be included in all copies or substantial portions of the software.
