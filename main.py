# 345678901234567890123456789012345678901234567890123456789012345678900123456789

# import local modules
import menu_modules.help as help
import menu_modules.view as view
import menu_modules.add as add
import menu_modules.edit as edit
import menu_modules.shared_variables as shvar

# import csv for csv file handling, import keyboard for hotkey use
# import sys for clean exit, import os to clear terminal
import sys
import os
import time
import csv
import pandas as pd


#######################################################################################################
# Main Menu
#######################################################################################################



# Variables and contastant definitions

invalid_selection = "That is not an option. Please try again."
upcoming_brithdays = []
upcoming_contacts = []
# cram_columns imported from view.py
# cram_storage_file imported from view.py


# Creates standard centred underline
def underline_centre():
    project_underline = 12 * "="
    print(f"{project_underline.center(80)}\n")

# Clears terminal and presents welcome message
def welcome():
    project_welcome = f"Welcome to CRaM, the best CRM in 2023."
    os.system('clear')
    underline_centre()
    print(f"{project_welcome.center(80)}\n")
    underline_centre()

# presents main menu and takes input
def main_menu_selection():
    while True:
        welcome()
        print(f"Main Menu:")
        for item in shvar.main_menu:
            print(f"{item}. {shvar.main_menu.get(item)}")
        menu_selection = input("> ")
        if menu_selection in shvar.main_menu_options:
            return menu_selection
        else:
            print(f"\n{invalid_selection}\n")
            time.sleep(1)

def action_main_menu(menu_selection):
    if menu_selection == shvar.main_menu_options[0]: # View
        view.view_flow()
        # break
    elif menu_selection == shvar.main_menu_options[1]: # Add
        print("Add a contact.")
        add.add_flow()
        # break
    elif menu_selection == shvar.main_menu_options[2]: # Edit
        print(f"action_main_menu: {menu_selection}") # test
        # break
    elif menu_selection == shvar.main_menu_options[3]: # Help
        os.system("clear")
        help.main_menu_help.display_help()
        input("\nPress enter to continue ... ")
        # break
    elif menu_selection == shvar.main_menu_options[4]: # Quit
        os.system("clear")
        print(f"Thanks for using CRaM.")
        sys.exit()


#######################################################################################################
# Main menu flow
#######################################################################################################

# checks if cram_storage.csv exists


def main_flow():
    while True:
        menu_selection = main_menu_selection()
        action_main_menu(menu_selection)


shvar.file_check()
main_flow()
