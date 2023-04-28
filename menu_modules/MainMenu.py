# import os to clear terminal, import sys for a clean exit, 
# import time for sleep, import keyboard for hotkey use
import os
import sys
import time
import keyboard

# importing created modules
import menu_modules.help as help

main_menu = { "1": "View Contacts",
              "2": "Add Contacts",
              "3": "Edit Contacts",
              "9": "Help",
              "0": "Quit CRaM",
             }

# Variables and contastant definitions
VALID_MAIN_MENU_OPTIONS = list(main_menu.keys())
project_name = "CRaM"
project_welcome = "Welcome to CRaM, the best CRM in 2023."
project_main_menu_heading = "Main Menu:"
PROJECT_INVALID_SELECTION = "That is not an option. Please try again."
upcoming_brithdays = []
upcoming_contacts = []

# Creates standard centred underline
project_underline = 12 * "="
def underline_centre():
    print(f"{project_underline.center(80)}\n")

# Clears terminal and presents welcome message
def welcome():
    os.system('clear')
    print(f"{project_name.center(80)}\n")
    underline_centre()
    print(f"{project_welcome.center(80)}\n")
    underline_centre()

# takes presents main menu and takes input
def main_menu_selection():
    while True:
        welcome()
        print(f"{project_main_menu_heading}")
        for item in main_menu:
            print(f"{item}. {main_menu.get(item)}")
        menu_selection = input("> ")
        if menu_selection in VALID_MAIN_MENU_OPTIONS:
            return(menu_selection)
        else:
            print(f"\n{PROJECT_INVALID_SELECTION}\n")
            time.sleep(1)

# actions main menu input
def action_main_menu(menu_selection):
    while True:
        if menu_selection == VALID_MAIN_MENU_OPTIONS[0]: # view contacts
            print(f"action_main_menu: {menu_selection}") # test
            break
        elif menu_selection == VALID_MAIN_MENU_OPTIONS[1]: # add contacts
            print(f"action_main_menu: {menu_selection}") # test
            break
        elif menu_selection == VALID_MAIN_MENU_OPTIONS[2]:
            print(f"action_main_menu: {menu_selection}") # test
            break
        elif menu_selection == VALID_MAIN_MENU_OPTIONS[3]:
            os.system("clear")
            help.MainMenuHelp()
            return input(keyboard.send("enter")) ### TODO - Fix, does not work ###
        elif menu_selection == VALID_MAIN_MENU_OPTIONS[4]:
            os.system("clear")
            print(f"Thanks for using {project_name}")
            sys.exit()
        # else:
        #     print(f"action_main_menu: {menu_selection}") # test