# 345678901234567890123456789012345678901234567890123456789012345678900123456789
import os
import sys
import time
# from help import main_menu_help

main_menu = { "1": "View Contacts",
              "2": "Add Contacts",
              "3": "Edit Contacts",
              "9": "Help",
              "0": "Quit CRaM",
             }

VALID_MAIN_MENU_OPTIONS = main_menu.keys()
project_name = "CRaM"
project_welcome = "Welcome to CRaM, the best CRM in 2023."
project_underline = 12 * "="
project_main_menu_heading = "Main Menu:"
PROJECT_INVALID_SELECTION = "That is not an option. Please try again."

main_menu_input = ""
upcoming_brithdays = []
upcoming_contacts =[]

# Creates standard centred underline
def underline_centre():
    print(f"{project_underline.center(80)}\n")

# Clears terminal screen and presents welcome message
def welcome():
    os.system('clear')
    print(f"{project_name.center(80)}\n")
    underline_centre()
    print(f"{project_welcome.center(80)}\n")
    underline_centre()

# takes input from main menu
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
    if menu_selection == VALID_MAIN_MENU_OPTIONS:
        print(f"action_main_menu: {menu_selection}") # test
    elif menu_selection == "2":
        print(f"action_main_menu: {menu_selection}") # test
    elif menu_selection == "3":
        print(f"action_main_menu: {menu_selection}") # test
    elif menu_selection == "9":
        print(f"action_main_menu: {menu_selection}") # test
    elif menu_selection == "0":
        print(f"action_main_menu: {menu_selection}") # test
        sys.exit()
    else:
        print(f"action_main_menu: {menu_selection}") # test


menu_selection = main_menu_selection()
action_main_menu(menu_selection)

