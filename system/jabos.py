
#--------------------------------------------------------------------------------

# The "operating system" of jabo

#--------------------------------------------------------------------------------


from time import sleep
from system.display import Display
from system.button import Button
import etc.app

#--------------------------------------------------------------------------------

a = Button('a')
b = Button('b')
up = Button('up')
down = Button('down')
display = Display()

#--------------------------------------------------------------------------------

def splash_screen():
    if etc.app.splash_delay > 0:
        display.clear()
        display.text(centered_text('jabo'), 0, display.line(2))
        display.text(centered_text(etc.app.version), 0 , display.line(3))
        display.show()
        sleep(etc.app.splash_delay)

#--------------------------------------------------------------------------------

class NavItem:
    def __init__(self, name, options, parent):
        self.name = name
        self.options = options # List of other nav items 
        self.parent = parent # NavItem of "Go back"
        
        
class AppItem:
    def __init__(self, name, app):
        self.name = name
        self.app = app
    
    def run(self):
        self.app.run()
            
#--------------------------------------------------------------------------------

class MenMap:
    '''
    MenMap handles the routing of the navigation side of JaboOS. It's responsible
    for returning a list of "submenus" based on the NavItem the user has selected.
    
    '''
    # Please don't add any cringe ":" or "->" to me please, 
    # my dad will handle it
    def __init__(self, root):
        self.active = root  # NavItem object
        self.options = self._load_options()
        self.sub_menus = self.active.options

    def _load_options(self):
        # Create a list of strings of the option names to
        # display to the user 
        menu_options = [x.name for x in self.active.options]
        if self.active.name != 'Main':
            menu_options.append('Go back')
        return menu_options
        
    def _load_menu_object(self, navitem):
        # Set attributes based on the new active item
        self.active = navitem 
        self.sub_menus = self.active.options
        self.options = self._load_options()
        return self.options 

    def go(self, nav_name):
        if nav_name == 'Go back':
            self._load_menu_object(self.active.parent)
        else:
            for menu in self.sub_menus:
                # Find the object from the given name
                if menu.name == nav_name:
                    if type(menu) == NavItem:
                        self._load_menu_object(menu)
                        break
                    elif type(menu) == AppItem:
                        menu.run()
        return self.options
        

class MenuWalker:
    ''' 
    Handles the "physical" side of the application browser. 
    Manages how text is displayed on screen, what user input does, 
    and then relays that information to MenMap to update the 
    current options. 
    '''
    # Scroll through a list of options, user selects one,
    # and is navigated accordingly. 
    def __init__(self, root):
        self.run_flag = True            
        self.cursor = '<-'
        self.cursor_pos = 'end'                 # can be before or after the string (start/end)
        self.menmap = MenMap(root)
        self.options = self.menmap.options      # List of NavItem names shown to the user to choose from
        self.active_item = self.options[0]      # Option currently selected by the cursor
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
        self.active_item_index = 0 # Reset the cursor to the top
        self.options = self.menmap.go(self.active_item) # Get the new list of submenus
        self.active_item = self.options[self.active_item_index]
        self.show_options()     # Refresh the screen
        
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

