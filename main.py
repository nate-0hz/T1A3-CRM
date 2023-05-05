# 345678901234567890123456789012345678901234567890123456789012345678900123456789

# import local modules
import menu_modules.help as help
import menu_modules.view as view
import menu_modules.add as add
import menu_modules.edit as edit

# import csv for csv file handling, import keyboard for hotkey use
# import sys for clean exit, import os to clear terminal
import sys
import os
import csv
import time
import pandas as pd


#######################################################################################################
# Main Menu
#######################################################################################################

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
# cram_columns = ["first_name", "last_name", "phone", "company", "email", "birthday", "last_contact", "next_contact"]
upcoming_brithdays = []
upcoming_contacts = []
cram_file = "cram_storage3.csv" ### Change this ###

try:
    cram_storage_view = pd.read_csv(cram_file)
except: ### Revisit this ###
    pass

# checks if cram_storage.csv exists
def file_check():
    try:
        pd.read_csv(cram_file)
        # cram_storage_read
    except FileNotFoundError:
        os.system("clear")
        print("You do not have a database for CRaM.")
        create_storage = input("Would you like to create one now? (y/n): ")
        if create_storage == "y":
            with open(cram_file, "w") as f:
                writer = csv.writer(f)
                writer.writerow(cram_columns) ### Revisit this ###
                f.close()
        else:
            os.system("clear")
            print("CRaM cannot continue without a database.")
            sys.exit()

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
        # break
    elif menu_selection == main_menu_options[2]: # Edit
        print(f"action_main_menu: {menu_selection}") # test
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


#######################################################################################################
# Main menu flow
#######################################################################################################

def main_flow():
    while True:
        menu_selection = main_menu_selection()
        action_main_menu(menu_selection)



file_check()
main_flow()
