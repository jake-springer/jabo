# 2/19/24
# The "operating system" of jabo

from time import sleep
from display import Display
from button import Button
import app

a = Button('a')
b = Button('b')
up = Button('up')
down = Button('down')

display = Display()

splash_delay = 1


def splash_screen():
    display.clear()
    display.text(centered_text('jabo'), 0, display.line(2))
    display.text(centered_text(app.version), 0 , display.line(3))
    display.show()
    sleep(splash_delay)

def centered_text(text):
    total_pad = display.max_chars - len(text)
    pad_side = round(total_pad / 2)
    space = ' ' * pad_side
    padded_text = space + text + space
    return padded_text

splash_screen()

        
        

    


