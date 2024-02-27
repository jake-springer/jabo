# 2/15/24

from machine import I2C, Pin
from system.jabos import splash_screen
from system.jabrowser import browser

# ------------------------------------------------------

led = Pin("LED", Pin.OUT)
power_led = Pin(15, Pin.OUT)
led.on()
power_led.on()

splash_screen()
browser.run()


#--------------------------------------------------------
