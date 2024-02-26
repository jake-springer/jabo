# 2/19/24

import sys 
sys.path.append('./apps')

from machine import I2C, Pin
from utime import sleep
from ssd1306 import SSD1306_I2C
from time import sleep
from display import Display
from button import Button
from ui import MenuWalker, splash_screen
# from apps import pong
# from lib import input_handler

# ------------------------------------------------------

led = Pin("LED", Pin.OUT)
power_led = Pin(15, Pin.OUT)
led.on()
power_led.on()

a = Button('a')
b= Button('b')
down = Button('down')
up = Button('up')
#
splash_screen()


m = MenuWalker()
m.run()

# input = input_handler.input_handler(a, b, down, up)
# pong.start_game(input)

#--------------------------------------------------------
