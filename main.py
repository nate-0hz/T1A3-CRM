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

################################################################################
# Main Menu
################################################################################

# main menu dict
main_menu = { "1": "View Contacts",
              "2": "Add Contacts",
              "3": "Edit Contacts",
              "9": "Help",
              "0": "Quit CRaM",
             }
# Variables and contastant definitions
main_menu_options = list(main_menu.keys())
invalid_selection = "That is not an option. Please try again."


# Clears terminal and presents welcome message
def welcome():
    project_welcome = f"Welcome to CRaM, the best CRM in 2023."
    os.system('clear')
    shvar.underline_centre()
    print(f"{project_welcome.center(80)}\n")
    shvar.underline_centre()

# presents main menu and takes input
def main_menu_selection():
    while True:
        welcome()
        print(f"Main Menu:")
        for item in main_menu:
            print(f"{item}. {main_menu.get(item)}")
        menu_selection = input("> ")
        if menu_selection in main_menu_options:
            return menu_selection
        else:
            print(f"\n{invalid_selection}\n")
            time.sleep(1)

def action_main_menu(menu_selection):
    if menu_selection == main_menu_options[0]: # View
        view.view_flow()
        # break
    elif menu_selection == main_menu_options[1]: # Add
        print("Add a contact.")
        add.add_flow()
        # break
    elif menu_selection == main_menu_options[2]: # Edit
        print(f"Edit a contact.") # test
        edit.edit_flow()
        # break
    elif menu_selection == main_menu_options[3]: # Help
        os.system("clear")
        help.main_menu_help.display_help()
        input("\nPress enter to continue ... ")
        # break
    elif menu_selection == main_menu_options[4]: # Quit
        os.system("clear")
        print(f"Thanks for using CRaM.")
        sys.exit()

################################################################################
# Main menu flow
################################################################################

def main_flow():
    while True:
        menu_selection = main_menu_selection()
        action_main_menu(menu_selection)


shvar.file_check()
main_flow()

