# 345678901234567890123456789012345678901234567890123456789012345678900123456789

# import local modules
import menu_modules.MainMenuFunctions as main
import menu_modules.help as help

# import csv for csv file handling, import keyboard for hotkey use
# import sys for clean exit, import os to clear terminal
import sys
import os
import pandas as pd

#######################################################################################################
# Main menu flow
#######################################################################################################

def main_flow():
    while True:
        menu_selection = main.main_menu_selection()
        action_main_menu(menu_selection)

# actions main menu input
def action_main_menu(menu_selection):
    while True:
        if menu_selection == main.menu_options[0]: # view contacts
            print(f"action_main_menu: {menu_selection}") # test
            break
        elif menu_selection == main.menu_options[1]: # add contacts
            print("Add a contact.")
            main.add_entry()
            break
        elif menu_selection == main.menu_options[2]:
            print(f"action_main_menu: {menu_selection}") # test
            break
        elif menu_selection == main.menu_options[3]:
            os.system("clear")
            help.MainMenuHelp()
            break
        elif menu_selection == main.menu_options[4]:
            os.system("clear")
            print(f"Thanks for using {main.project_name}")
            sys.exit()


#######################################################################################################
# Add record flow
#######################################################################################################



#######################################################################################################
# View Contact
#######################################################################################################

# Display all records
def search():
    pass

# Search for record

#Return to main menu


#######################################################################################################
# Main Flow control
#######################################################################################################



main.file_check()
main_flow()
