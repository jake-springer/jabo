# jabo
Handheld device using the Raspberry Pi Pico W

## Buttons 
### Creating Buttons
Buttons are called with `Button("_{button_name}_")`. Options are `a`, `b`, `up`, and `down`. <br> Example: `jump = Button('a')`


### Check Button State
The `is_pressed()` method returns True if the button is pressed _in that moment_, and it's recommended to add a sleep()
call after a press is detected to prevent multiple unintended triggers. 

## Display
### Display Attributes
The Display library is used to control the GPIO pins of the Pico, but also manage the specific 
traits of the screen itself. Different attributes can be used to programatically format text and
other on screen elements. 

- char_width = 8
  - Amount of horizontal pixels a character in the standard font takes up.
- line_height = 14
  - Amount of pixels each line of text takes up.
- max_chars = 16
  - Amount of characters in the standard font that can fit comfortably on a single line.
- max_lines = 5
  - Amount of lines of text that can be displayed at once.
 
This can also be thought of as a grid measured 16x5, with each space measuring 14px x 8px. 

### Methods
- `line(line_no)`: Useful for quickly positioning a line of text on screen. line_no is an integer between 1-5.
- `clear()`: Removes everything on the screen. 
