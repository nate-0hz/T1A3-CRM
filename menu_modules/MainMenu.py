# import os to clear terminal, import sys for a clean exit, 
# import time for sleep, import keyboard for hotkey use
import os
import time

# importing created modules


# main menu dict
main_menu = { "1": "View Contact",
              "2": "Add Contact",
              "3": "Edit Contact",
              "9": "Help",
              "0": "Quit CRaM",
             }

# Variables and contastant definitions
project_name = "CRaM"  
menu_options = list(main_menu.keys())
invalid_selection = "That is not an option. Please try again."
upcoming_brithdays = []
upcoming_contacts = []

# Creates standard centred underline
def underline_centre():
    project_underline = 12 * "="
    print(f"{project_underline.center(80)}\n")

# Clears terminal and presents welcome message
def welcome():
    project_welcome = f"Welcome to {project_name}, the best CRM in 2023."
    os.system('clear')
    print(f"{project_name.center(80)}\n")
    underline_centre()
    print(f"{project_welcome.center(80)}\n")
    underline_centre()

# presents main menu and takes input
def main_menu_selection():
    while True:
        welcome()
        print(f"Main Menu:")
        for item in main_menu:
            print(f"{item}. {main_menu.get(item)}")
        menu_selection = input("> ")
        if menu_selection in menu_options:
            return(menu_selection)
        else:
            print(f"\n{invalid_selection}\n")
            time.sleep(1)

