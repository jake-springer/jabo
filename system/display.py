# 0.0.1

from system.ssd1306 import SSD1306_I2C
from machine import Pin, I2C
from time import sleep



class Display(SSD1306_I2C):
    def __init__(self):
        self.display_width = 128
        self.display_height = 64
        self.refresh_rate = 400000
        
        self.char_width = 8 #px
        self.line_height = 14 #px
        
        self.max_chars = 16
        self.max_lines = 5

        self.sda = Pin(0)
        self.scl = Pin(1)

        i2c = I2C(0, sda=self.sda, scl=self.scl, freq=self.refresh_rate)
        super().__init__(self.display_width, self.display_height, i2c)
        #self.clear()

    def line(self, line_no):
        # Get the pixel position of a line of text with a number 1-5
        if line_no == 'center':    #  Lil alias for ease of use
            return 1 * self.line_height
        # subtract 1 to make up for 0 index & i'm stupid
        return (line_no - 1) * self.line_height
    
    def clear(self):
        self.fill(0)
        self.show()


    def blink(self, x):
        self.clear()
        count = 0
        while count < x:
            self.fill(1)
            self.show()
            sleep(0.1)
            self.clear()
            sleep(0.1)
            count += 1
    

        