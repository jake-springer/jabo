# Menu mappings for what-goes-where and where-that-leads
# Menu mapping have two keys:
#	- name:
#		- Alias for the menu, must match an option in another list
#	- options:
#		- The list of options given to the user when that menu is
#	      considered "active"

menus = {

    {"Name": ["Apps", "Games", "Settings"]},
    {"Settings": ["Brightness", "Refresh Rate", "Contrast"]},
    {"Apps": ["Calculator", "Contacts", "Buzzer"]}

}

main_menu = { # Basically the home screen
    "name":"Main",
    "options":["Apps", "Games", "Settings"]
    }

settings_menu = {
    "name":"Settings",
    "options":[]
    }

apps_menu = {
    "name":"Apps",
    "options":[
        "Calculator",
        "Contacts",
        "Buzzer"
        ]
    }

all_menus = [main_menu, settings_menu, apps_menu]

# Add "Go back" to each options list, except Main
for m in all_menus[1:]:
    m["options"].append("Go back")

class MenuMap:
    def __init__(self):
        self.current_menu = all_menus[0] # main menu
        self.menu_name = self.current_menu["name"]
        self.options = self.current_menu["options"]
        self.trail = [] # Where the user was last
        
    def _load_menu(self, menu_name):
        # Change object attributes to the values for the new menu 
        for m in all_menus:
            if m["name"] == menu_name:
                self.current_menu = all_menus[all_menus.index(m)]
                break
        self.menu_name = self.current_menu['name']
        self.options = self.current_menu['options']
        
    def go_back(self):
        try:
            if self.trail[-1] == 'Go back':
                return self.go() # Prevents getting stuck because last in trail is "go back"
            self.current_menu = self.trail[-1]
            return self.go(self.current_menu)
        except IndexError:
            return self.go() # Reset to main menu
    
    def go(self, menu_name="Main"):
        # Go to a given menu, will return to main by default 
        self.trail.append(self.current_menu)
        self._load_menu(menu_name)
        return self.options
