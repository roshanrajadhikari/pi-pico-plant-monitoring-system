<h1 align="center" id="title">Pi Pico Plant Monitoring System</h1>

<p align="center"><img src="https://socialify.git.ci/roshanrajadhikari/pi-pico-plant-monitoring-system/image?description=1&amp;font=Inter&amp;forks=1&amp;issues=1&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Circuit%20Board&amp;pulls=1&amp;stargazers=1&amp;theme=Dark" alt="project-image"></p>

<p id="description">Micropython powred Pi Pico for plant monitoring using MQTT communication.</p>
# IoT Plant Monitoring System

An automated, multi-threaded IoT telemetry system designed to monitor and report soil moisture, temperature, and environmental conditions in real time using edge hardware.

## 🚀 Key Features
* **Asynchronous Telemetry:** Built with multi-threaded script logic to handle simultaneous sensor scanning and network communication without blocking execution.
* **Lightweight Transport:** Utilizes the MQTT protocol to stream lightweight JSON payloads to a centralized broker.
* **Resilient Networking:** Implemented auto-reconnect fallback logic for stable Wi-Fi connectivity at the edge.

## 🛠️ Tech Stack & Hardware
* **Languages:** MicroPython / Python
* **Hardware Target:** Raspberry Pi Pico W / ESP32
* **Protocols:** MQTT, I2C, Wi-Fi 802.11 b/g/n
* **Sensors:** Capacitive Soil Moisture Sensors, DHT22 (Temperature/Humidity)

## 📁 Repository Structure
```text
├── src/
│   ├── main.py        # Application entry point and thread management
│   ├── mqtt_client.py # Broker connection handles and message publishing
│   └── sensors.py     # Hardware abstraction layers for connected modules
├── schematics/        # Hardware wiring diagrams and pinout configurations
└── README.md
