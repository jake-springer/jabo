# 0.0.1

from machine import Pin
from time import sleep

# Class for reading the button hardware information from the Pico

# Buttons are arranged in a classic GameBoy layout, 
# just missing the left and right D pad buttons. 

a_pin = 18
b_pin = 19
down_pin = 20
up_pin = 21 

pin_mapping = {
    'a': 18,
    'b': 19,
    'down': 20,
    'up': 21
}

class Button(Pin):
    def __init__(self, alias):
        self.alias = alias
        self.pin = pin_mapping[self.alias]
        super().__init__(self.pin, Pin.IN, Pin.PULL_UP)
    
    def is_pressed(self):
        if self.value() == 0:   # Pin goes low when pressed 
            return True 
        return False 


        


