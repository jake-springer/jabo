# 0.0.1

from machine import I2C, Pin
from utime import sleep
from ssd1306 import SSD1306_I2C
from time import sleep
from display import Display
from button import Button

# ------------------------------------------------------

# led = Pin("LED", Pin.OUT)
# while True:
#     led.toggle()
#     sleep(1)

display = Display()

a = Button('a')
b = Button('b')
down = Button('down')
up = Button('up')

buttons = [a, b, down, up]

while True:
    for b in buttons:
        if b.is_pressed():
            display.simple_text(f"{b.alias} was pressed!")
            sleep(0.5)

#--------------------------------------------------------
