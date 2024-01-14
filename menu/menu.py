import utime
from menu.menulist import menu_list

class Menu:
    def __init__(self,broker):
        self.is_running = False #main flag
        self.broker = broker
        self.menu_list = menu_list
        self.current_menu = menu_list

    def display(self,menu_options):
        self.__cls()
        print("Plant Monitoring System")
        for index, menu_item in enumerate(menu_options, start=1):
            print(f"{index}.{menu_item['option']}")

    def __cls(self):
        print("\033c")
    
    #function to handle calling functions
    def __function(self,name):
        if name == "exit_menu": 
            #handle exit
            self.exit_menu()
        elif name == "view_sensors":
            #display sensors
            self.view_sensors()
        else:
            #no implemented function found
            print(f"No function named {name}")
            utime.sleep(1) #wait a sec


    #handle users choice
    def make_choice(self, choice):
        #exception handle
        try:
            index = int(choice) - 1
            selected_menu = self.current_menu[index]
            # Check if selected item has submenu
            if "submenu" in selected_menu:
                self.current_menu = selected_menu["submenu"]
            #or else it should be a function
            else:
                self.__function(selected_menu["function"]) #handle function
        except ValueError:
            pass

    def start(self):
        self.is_running = True  # set the flag to running
        while self.is_running:
            self.display(self.current_menu)
            # Check if there's any user input available
            choice = input(f">:") #wait for user choice
            self.make_choice(choice)

    def exit_menu(self):
        # If in a submenu, go back; otherwise, exit the main loop
        if self.current_menu is not self.menu_list:
            self.current_menu = self.menu_list
        else:
            self.is_running = False #stop running
    
    #function that displays sensors in list and the values
    def view_sensors(self):
        stop = False #flag to stop the loop
        try:  
            while not stop:
                values = self.broker.getSensors()
                self.__cls()
                for value in values:
                    print(f"Sensor : {value}")
                utime.sleep(3)
        except KeyboardInterrupt: #handle interruption
            print("Interrupt: Exiting")
            stop = True #if there was interruption set flag to true
            utime.sleep(0.5) #wait half a sec
            
            


    