from ..sys.button import Button

# Input handler should be an object within each game
# Instantiate the class with objects of each button
class input_handler:
    def __init__(self, a: Button, b: Button, down: Button, up: Button):
        self.buttons = {
            'a': a,
            'b': b,
            'down': down,
            'up': up
        }
        
        # Use these within game to check if (True: button is pressed | False: button is not pressed)
        self.a = False
        self.b = False
        self.down = False
        self.up = False
    
    # In game loop call tick at start of function
    def tick(self):
        self.a = self.buttons['a'].is_pressed()
        self.b = self.buttons['a'].is_pressed()
        self.down = self.buttons['a'].is_pressed()
        self.up = self.buttons['a'].is_pressed()