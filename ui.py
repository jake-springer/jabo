# The "operating system" of jabo

from time import sleep
from display import Display
from button import Button
import app
from menus import MenuMap

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


def break_lines(text):
    # Break long lines of text into smaller chunks that can be shown on screen
    lines = []    
    words = text.split(" ")
    current_line = words[0]
    for w in words[1:]:
        if len(current_line) + len(w) >= display.max_chars: # Reached character limit
            lines.append(current_line) # Add the full line
            current_line = w # Reset for next line
        else:
            current_line = current_line + ' ' + w 
    lines.append(current_line) # Add anything left over
    return lines 
    
#--------------------------------------------------------------------------------

class TextBox:
    def __init__(self, text):
        self.text = text
        self.lines = break_lines(self.text)
        self.current_line = 0 # The line at the top of the screen
        self.run_flag = True
        if len(self.lines) <= 5:
            self.put_text()
        else:
            self.scroller()
        
    def put_text(self, display_lines=None):
        # Put formatted text on the screen line by line
        display.clear()
        if not display_lines:
            display_lines = self.lines
        row = 1
        for l in display_lines:
            display.text(l, 0, display.line(row))
            row += 1
        display.show()
    
    def await_nav(self):
        if b.is_pressed():
            self.run_flag = False
            sleep(0.5)
            return
        elif down.is_pressed():
            self.scroll_down()
            return
        elif up.is_pressed():
            self.scroll_up()
    
    def scroll_up(self):
        if self.current_line - 1 < 0:
            return
        self.current_line -= 1
        self.put_text(display_lines = self.lines[self.current_line:])
        sleep(0.2)
    
    def scroll_down(self):
        new_line = self.current_line + 1
        # Do nothing if at the end
        try:
            x = self.lines[new_line + 4] # Check if anything exists after what is displayed
        except IndexError:
            return
        # Update the screen with new text
        self.put_text(display_lines=self.lines[new_line:])
        self.current_line += 1
        sleep(0.2)
    
    def scroller(self):
        # Used to move through text.
        # Think of the 'less' utility in Linux
        self.put_text()
        while self.run_flag:
            self.await_nav()



#--------------------------------------------------------------------------------


class MenuWalker:
    def __init__(self):
        self.run_flag = True
            
        self.cursor = '<-'
        self.cursor_pos = 'end' # can be before or after the string (start/end)
    
        self.menmap = MenuMap()
        self.options = self.menmap.options
        self.active_item = self.options[0]  # Option currently selected by the cursor
        self.active_item_index = 0

    def nav_up(self):
        # Move up (backwards) in the list
        if self.active_item_index == 0: # at top
            return
        self.active_item_index -= 1
        self.active_item = self.options[self.active_item_index]
        self.show_options()

        
    def nav_down(self):
        # Move down (forward) in the list
        if self.active_item_index == len(self.options) - 1: # at bottom
            return
        self.active_item_index += 1
        self.active_item = self.options[self.active_item_index]
        self.show_options()
    
    def _switch_menu(self):
        self.active_item_index = 0
        if self.active_item == 'Go back':
            print("[UI] Selected 'Go back'")
            self.options = self.menmap.go_back()
        else:
            self.options = self.menmap.go(self.active_item)
            print(f"[UI] Selected '{self.active_item}'")
        self.active_item = self.options[self.active_item_index]
        self.show_options()
        
    def await_input(self):
        if up.is_pressed():
            self.nav_up()
        elif down.is_pressed():
            self.nav_down()
        elif a.is_pressed():
            self._switch_menu()
        elif b.is_pressed():
            pass
        else:
            pass
        sleep(0.1)
        return
        
    def show_options(self):
        display.clear()
        l = 1  # Line on screen
        print(self.options)
        print(self.active_item)
        #input()
        for o in self.options[self.options.index(self.active_item):]:
            if o == self.active_item:
                # Modify the line to include the cursor
                if self.cursor_pos == 'start':
                    o = self.cursor + ' ' + o
                elif self.cursor_pos == 'end':
                    o = o + ' ' + self.cursor
            # Add the line to the display
                display.text(o, 0, display.line(l))
            else:
                display.text(o, 0, display.line(l))
            l += 1
        # Refresh the display
        display.show()
        return 
            
    def run(self):
        self.show_options()
        while self.run_flag:
            self.await_input()

#--------------------------------------------------------------------------------