# menulist.py
menu_list = [
    {"option": "View Sensors", "function": "view_sensors"},
    {
        "option": "More Settings Here",
        "submenu": [
            {"option": "Calibrate Sensor", 
             "submenu": [
                {"option": "Start Calibration", "function": "start_calibration"},
                {"option": "Go Back", "function": "exit_menu"}
                ]
            },
            {"option": "Configure Settings", "function": "configure_settings"},
            {"option": "Go Back", "function": "exit_menu"},
        ],
    },
    {"option": "Exit", "function": "exit_menu"},
]

