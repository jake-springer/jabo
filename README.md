# jabo
Handheld device using the Raspberry Pi Pico W

## Buttons 
Buttons are called with `Button("_{button_name}_")`. Options are `a`, `b`, `up`, and `down`.  
The `is_pressed()` method returns True if the button is pressed _in that moment_, and it's recommended to add a sleep()
call after a press is detected to prevent multiple unintended triggers. 
