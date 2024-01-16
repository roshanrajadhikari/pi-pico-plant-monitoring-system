import utime
from menu.menulist import menu_list
from machine import Pin

# Set the GPIO pin you've connected to as an input
touch_pin = Pin(14, Pin.IN, Pin.PULL_DOWN)

class Menu:
    def __init__(self, broker):
        # Initialize the Menu object
        self.is_running = False  # Main flag
        self.broker = broker
        self.menu_stack = [menu_list]

    def display(self, menu_options):
        # Display the menu options on the screen
        self.__cls()
        print("Plant Monitoring System")
        for index, menu_item in enumerate(menu_options, start=1):
            print(f"{index}. {menu_item['option']}")

    # Clear the screen
    def __cls(self):
        print("\033c")

    # Function to handle calling functions
    def __function(self, name):
        if name == "exit_menu":
            # Handle exit menu option
            self.exit_menu()
        elif name == "view_sensors":
            # Display sensor values
            self.view_sensors()
        else:
            # No implemented function found
            print(f"No function named {name}")
            utime.sleep(1)  # Wait a second

    # Handle user's menu choice
    def make_choice(self, choice):
        current_menu = self.menu_stack[-1]  # Get the latest element in array, the current menu
        # Exception handling
        try:
            index = int(choice) - 1  # Convert choice to index
            if index < 0 or index > (len(current_menu) - 1):
                # Invalid menu choice
                print("No choice available")
                utime.sleep(0.5)  # Wait a bit
            else:
                selected_menu = current_menu[index]
                # Check if selected item has a submenu
                if "submenu" in selected_menu:
                    self.menu_stack.append(selected_menu['submenu'])  # Add selected menu to the menu stack
                else:
                    # It should be a function
                    self.__function(selected_menu["function"])  # Handle function
        except ValueError as e:
            pass  # Ignore invalid input

    def start(self):
        # Start the main menu loop
        self.is_running = True
        while self.is_running:
            self.display(self.menu_stack[-1])
            # Check if there's any user input available
            choice = input(">:")  # Wait for user choice
            self.make_choice(choice)

    def exit_menu(self):
        # Handle exit menu option
        if len(self.menu_stack) == 1:
            self.is_running = False  # Exit out of the main loop
        else:
            self.menu_stack.pop()  # Go back to the previous menu

    # Function that displays sensor values in a list
    def view_sensors(self):
        try:
            while not touch_pin.value():  # While the button is not pressed
                data = self.broker.getSensors()
                self.__cls()
                for item in data:
                    print(f"{item['name']} : {item['value']}")
                    print("Push the button to exit")
                utime.sleep(0.1)
        except KeyboardInterrupt:
            print("Interrupt: Exiting")
            utime.sleep(0.5)  # Wait half a second
        except Exception as e:
            print(f"Error: {e}")
