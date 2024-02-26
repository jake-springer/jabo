# 2/15/24

from machine import I2C, Pin
from utime import sleep
from time import sleep
from system.display import Display
from system.button import Button
from lib.ui import splash_screen
from lib.ui import MenuWalker

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

#--------------------------------------------------------
