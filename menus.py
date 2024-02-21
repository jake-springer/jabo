# Menu mappings for what-goes-where and where-that-leads
# Menu mapping have two keys:
#	- name:
#		- Alias for the menu, must match an option in another list
#	- options:	The list of options given to the user when that menu is
#	  considered "active"

class MenuMap:
    def __init__(self):
        self.name = None
        self.options = None
        

all_menus = [
    main_menu = {
        "name":"Main",
        "options":["Apps", "Games", "Settings"]
        },
    settings_menu = {
        "name":"Settings",
        "options":[]
        },
    apps_menu 
    ] 

