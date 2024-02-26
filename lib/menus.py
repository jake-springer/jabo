from system.display import Display 

display = Display()

class NavItem:
    def __init__(self, name, options, parent):
        self.name = name
        self.options = options # List of other nav items 
        self.parent = parent # NavItem of "Go back"
        if self.parent:
            self.options.append("Go back")


main = NavItem('Main', None, None)
apps = NavItem('Apps', [], main)
games = NavItem('Games', [], main)
settings = NavItem('Settings', [], main)

main.options = [apps, games, settings]

class MenMap:
    # Please don't add any cringe ":" or "->" to me please, 
    # my dad will handle it
    def __init__(self):
        self.active = main  # ItemNav object
        self.options = self._load_options() 

    def _load_options(self):
        # Create a list of strings of the option names to
        # display to the user 
        return [x.name for x in self.active.options]
        
    def _load_menu_object(self, navitem):
        # Set attributes based on the new active item
        self.active = navitem 
        self.options = self._load_options()
        return self.options 

    def go(self, nav_name):
        if nav_name == 'Go back':
            self._load_menu_object(self.active.parent)
        else:
            for menu in self.options:
                # Find the navitem object from the given name
                if menu.name == nav_name:
                    self._load_menu_object(menu)
                    break
        return self.options
        

class MenuWalker:
    # Scroll through a list of options, user selects one,
    # and is navigated accordingly. 
    def __init__(self):
        self.run_flag = True
        self.cursor = '<-'
        self.cursor_pos = 'end' # can be before or after the string (start/end)
        self.menmap = MenMap()
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
