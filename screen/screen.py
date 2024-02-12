import sys
from machine import Pin, I2C
from screen.ssd1306 import SSD1306_I2C


# Screen Variables
width = 128
height = 64
line = 0 
highlight = 1
shift = 0
list_length = 0
total_lines = 6
pointer = 0

class Screen:
    def __init__(self) -> None:
        self.i2c_dev = self.init_i2c(scl_pin=17, sda_pin=16)
        self.oled = SSD1306_I2C(width, height, self.i2c_dev)
        self.running = False


    def init_i2c(self,scl_pin, sda_pin):
        # Initialize I2C device
        i2c_dev = I2C(0, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=200000)
        i2c_addr = [hex(ii) for ii in i2c_dev.scan()]
        
        if not i2c_addr:
            print('No I2C Display Found')
            sys.exit()
        else:
            print("I2C Address      : {}".format(i2c_addr[0]))
            print("I2C Configuration: {}".format(i2c_dev))
        
        return i2c_dev
    
    def show(self, menu,title):
        """ Shows the given lines on the screen"""
        
        # bring in the global variables
        global line, highlight, shift, list_length, pointer

        
        line_height = 10 #set line height to 10
        
        # Shift the items so that it shows on the display
        #print(pointer)
        list_length = len(menu)        
        
        if self.running:
            line = 0
            # clear the display
            self.oled.fill_rect(0, 0, width, height, 0)
            
            #print the title
            self.oled.rect(0,0,width,line_height,1)
            self.oled.text(f"{title}", 0, line * line_height, 1) 
            line += 1 #increment line
            
            if highlight > (total_lines - 1): #if highlight is greater than 5 (total lines - 1 ; -title)
                shift = highlight - (total_lines - 1) #shift the menu items up by the difference 
            else:
                shift = 0   #else set shift to 0
            
            short_list = menu[shift:shift + (total_lines-1)] #get the menu items to be displayed
            line_height = 11 #set line height to 11
            
            #loop through the menu items
            for item_dict in short_list:
                text_color = 1 #set default text color to white
                item_length = len(item_dict)
                text = item_dict
                display_text = text #default display text is the same as text

                if highlight == (line + shift): #if highlight is equal to the current line
                    self.oled.fill_rect(0, line * line_height, width, line_height, 1) #highlight the line

                    text_color = 0 # set text color to black
                    
                    # scrolling text if text is longer than 14 characters (excluding the added space)
                    if item_length > 14:
                        text += " " #add space after text -> adds gap 
                        display_text = text[pointer:] + text[:pointer] #
                        pointer = (pointer + 1) % (item_length)  # Reset pointer if it reaches the end   
                #display line 
                self.oled.text(f"{display_text or text}", 0, line * line_height, text_color)
                line += 1
            self.oled.show()
            
    def set_highlight(self,x):
        global highlight, pointer
        highlight = x
        pointer = 0 
                  
    def off(self):
       
        self.oled.fill(0)
        self.oled.show()
             