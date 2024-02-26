
# App for displaying text to the user on a screen that was clearly
# never meant to display a lot of text

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



class Jabook:
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
