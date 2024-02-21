# 0.0.1

from ssd1306 import SSD1306_I2C
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
        if line_no == 'center':
            return 1 * self.line_height
        # subtract 1 to make up for 0 index & i'm stupid
        return (line_no - 1) * self.line_height
    
    def clear(self):
        self.fill(0)
        self.show()

    def blink(self, seconds):
        self.clear()
        count = 0
        while count < seconds:
            self.fill(1)
            self.show()
            sleep(0.5)
            self.clear()
            sleep(0.5)
            count += 1
        
    def line_break(self, text):
        lines = []
        current_line = ""
        words = text.split(" ")
        for w in words:
            too_long = len(current_line) + len(w) >= self.max_chars
            if too_long:
                lines.append(current_line)
                current_line = w
            else:
                current_line = current_line + ' ' + w
        lines.append(current_line) # Append whatever is left over
        return lines
    
    
    def show_text(self, given_text):
        self.clear()
        lines = self.line_break(given_text)
        current_line = 0
        for l in lines:
            self.text(l, 0, self.line(current_line))
            current_line += 1
        self.show()
        

    def simple_text(self, given_text):
        self.clear()
        self.text(given_text, 0, 0)
        self.show()
        
            
            

    

        