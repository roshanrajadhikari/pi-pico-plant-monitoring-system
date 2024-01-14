# menulist.py

menu_list = [
    {"option": "View Sensors", "function": "view_sensors"},
    {
        "option": "More Settings",
        "submenu": [
            {"option": "Calibrate Sensor", "function": "calibrate_sensor"},
            {"option": "Configure Settings", "function": "configure_settings"},
            {"option": "Go Back", "function": "exit_menu"},
        ],
    },
    {"option": "Exit", "function": "exit_menu"},
]
