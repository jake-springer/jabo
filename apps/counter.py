from system.button import Button 
from system.display import Display
from system.jabos import centered_text
from time import sleep

up_btn = Button('up')
down_btn = Button('down')
help_btn = Button('a')
exit_btn = Button('b')
display = Display()

class Counter:
    def __init__(self):
        self.count = None
        self.run_flag = True
        
    def setup(self):
        self.run_flag = True
        self.count = 0
        self.refresh()

    def count_up(self):
        self.count += 1 

    def count_down(self):
        self.count -= 1

    def refresh(self):    
        display.clear()
        display.text(
            centered_text(str(self.count)),
            0,
            display.line('center')
            )
        
        display.text(
            centered_text("A - Help"),
            0,
            display.line(5)
            )
        
        display.show()
        sleep(0.2)
        
    def display_help(self):
        display.clear()
        while True:
            display.text("UP - Increase", 0, display.line(1))
            display.text("DOWN - Decrease", 0, display.line(2))
            display.text("B - Exit program", 0, display.line(3))
            display.show()
            if exit_btn.is_pressed():
                break 
        

    def run(self):
        self.setup()
        while self.run_flag: 
            if exit_btn.is_pressed():
                self.run_flag = False
            else:
                if up_btn.is_pressed():
                    self.count_up()
                    self.refresh()
                elif down_btn.is_pressed():
                    self.count_down()
                    self.refresh()
                elif help_btn.is_pressed():
                    self.display_help()
                    self.refresh()
                
                
                
        self.run_flag = True # Reset the run flag for subsequent runs 

