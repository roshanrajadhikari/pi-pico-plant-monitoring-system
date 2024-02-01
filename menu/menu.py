import menu
import utime
from machine import Pin
import uasyncio as asyncio
from .menulist import menu_list
from screen.screen import Screen
 
#two states of Menu class
MENU = 1
DATA = 2

#get screen instance
screen = Screen()

class Menu:
    def __init__(self, broker):
        # Initialize the Menu object
        self.is_running = False  # Main flag
        self.using_screen = True # using screen flag
        self.broker = broker
        
        #UI variables
        self.dispay_stack = [menu_list]
        self.display_state = MENU
        self.highlight = 1
        self.pointer = 0

    def display(self, menu_options, title=None):
        # Display the menu options on the screen
        self.__cls()
        list2screen = []
        
        if(title == None):
            print("Plant Monitoring System")
        else:
            print(title)
            
        for index, menu_item in enumerate(menu_options, start=1):
            if index == self.highlight:
                front = ">"
            else:
                front = " "
                
            if self.display_state == MENU:
                print(f"{front}{index}. {menu_item['option']}")
                list2screen.append(f"{menu_item['option']}")
            elif self.display_state == DATA:
                print(f"{front}{menu_item['name']} : {menu_item['value']}")
                list2screen.append(f"{menu_item['name']}:{menu_item['value']}")    
            else :
                pass
        
        #print(list2screen,self.using_screen)
        if self.using_screen:
            screen.show(list2screen,title)
            
    # Clear the screen
    def __cls(self):
        print("\033c")

    # Function to handle calling functions
    def __function(self, name):
        self.display_state = MENU
        if name == "exit_menu":
            # Handle exit menu option
            self.exit_menu()
        elif name == "view_sensors":
            # Display sensor values
            self.display_state = DATA
            self.dispay_stack.append(self.broker.getSensors())
            #self.view_sensors()
        else:
            # No implemented function found
            print(f"No function named {name}")
            utime.sleep(1)  # Wait a second
        

    # Handle user's menu choice
    def make_choice(self, choice):
        current_menu = self.dispay_stack[-1]  # Get the latest element in array, the current menu
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
                    self.dispay_stack.append(selected_menu['submenu'])  # Add selected menu to the menu stack
                else:
                    # It should be a function
                    self.__function(selected_menu["function"])  # Handle function
        except ValueError as e:
            pass  # Ignore invalid input

    async def start(self):
        # Start the main menu loop
        self.reset()
        await asyncio.sleep_ms(200)
        try:
            if self.using_screen:
                screen.running = True
            else:
                screen.running = False
            try:
                self.is_running = True
                while self.is_running:
                    title = ""
                    if self.display_state == MENU:
                        title = "Plant Monitoring System"
                    elif self.display_state == DATA:
                        title = "Sensor Data"
                        self.dispay_stack.pop()
                        self.dispay_stack.append(self.broker.getSensors())
                    else:
                        pass
                    self.display(self.dispay_stack[-1],title)
                    ### OLD CODE ###
                    #print(self.highlight)
                    # Check if there's any user input available
                    #choice = input(">:")  # Wait for user choice
                    #self.make_choice(choice)
                    ### END OLD CODE ###
                    
                    await asyncio.sleep_ms(200)
            except KeyboardInterrupt:
                print("exiting...")
                self.exit_menu()
                
        except BaseException as e:
            print(f"Error in main loop @menu: {e}")
            self.is_running = False
        
        #when menu running flag is down turn off screen
        screen.off()
        
    def set_highlight(self,x):
        self.highlight = x
        self.pointer = 0
        screen.set_highlight(x)
        
    def cycle_highlight(self):
      
        if(self.highlight == len(self.dispay_stack[-1])): #if highlight is at the end of the list
            self.set_highlight(1) # set it back to the first item
        else:
            self.set_highlight((self.highlight+1)) #else increment it by 1

    def reset(self):
        self.set_highlight(1)
        #screen.reset()
 
    def handle_button_press(self,press_type):
        print("button pressed")
        if self.is_running: #do nothing if menu is not running
            
            if press_type == "long": #if long press
                if self.display_state == DATA: #if long press request was from data state
                    self.exit_menu()
                else:
                    self.make_choice(self.highlight) #make choice from current highlight

            
            elif press_type == "single": # if single press
                self.cycle_highlight() #cycle highlight
            else:
                pass
                
    def exit_menu(self):
        # Handle exit menu option
        
        if self.display_state == DATA: #if exit request was from data state
            self.display_state = MENU #set it back to menu (where it was last time in the menu)  
        
        if len(self.dispay_stack) == 1:
             self.is_running = False  # Exit out of the main loop
        else:
            self.dispay_stack.pop()  # Go back to the previous menu

