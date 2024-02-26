
# -----------------------------------------------------------------

# Application information used by jabOS to list/manage
# applications and their execution.

# -----------------------------------------------------------------
# (shouldn't really need to touch these)
from system.jabos import NavItem, AppItem

main_menu = NavItem('Main', None, None)
apps_menu = NavItem('Apps', [], main_menu)
games_menu = NavItem('Games', [], main_menu)
settings_menu = NavItem('Settings', [], main_menu)
main_menu.options = [apps_menu, games_menu, settings_menu]

# -----------------------------------------------------------------
# STEP 1: Import the application object

from apps.pong import Pong


# -----------------------------------------------------------------
# STEP 2: Create the app item with the title the app will have in
#         the browser

pong_app = AppItem('Pong', Pong())


# -----------------------------------------------------------------
# STEP 3: Add the app item to whatever list it belongs to

APPS = []
GAMES = [pong_app]
SETTINGS = []


# -----------------------------------------------------------------

apps_menu.options = APPS
games_menu.options = GAMES
settings_menu.options = SETTINGS

