# import os to clear terminal, import sys for a clean exit, 
# import time for sleep, import keyboard for hotkey use
import os
import time
import csv
import sys
import pandas as pd

# importing created modules
import classes.class_record as record


#######################################################################################################
# Main Menu
#######################################################################################################

# main menu dict
main_menu = { "1": "View Contact",
              "2": "Add Contact",
              "3": "Edit Contact",
              "9": "Help",
              "0": "Quit CRaM",
             }

# Variables and contastant definitions
menu_options = list(main_menu.keys())
invalid_selection = "That is not an option. Please try again."
cram_columns = ["fname", "lname", "phone", "company", "email", "birthday", "last_contact", "next_contact"]
upcoming_brithdays = []
upcoming_contacts = []
cram_file = "cram_storage.csv"

cram_storage_view = pd.read_csv(cram_file)

def cram_storage_new():
            with open(cram_file, "w") as f:
                writer = csv.writer(f)
                writer.writerow(cram_columns)
                f.close()

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
            cram_storage_new()
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
        if menu_selection in menu_options:
            return(menu_selection)
        else:
            print(f"\n{invalid_selection}\n")
            time.sleep(1)

#######################################################################################################
# Add Record
#######################################################################################################

def add_entry():
    input_name = input("What is the name to add? (leave blank and press return to exit) ")
    while input_name == "":
        break
    else:
        cram_storage = open(cram_file, "r")
        with cram_storage as open_file:
            doesExist = open_file.read()
            cram_storage.close()
            if input_name in doesExist:
                add_new = input(f"{input_name} already exists. Create new entry?(yes/no) ")
                if add_new == "yes":
                    gather_details(input_name)
                    # add_another()
                else:
                    return
            else:
                gather_details(input_name)
                # add_another()

def gather_details(input_name):
    phone = input("Add phone number: ")
    email = input("Add email: ")
    birthday = "" ### TODO ### ADD INPUT ###
    last_contact = "" ### TODO ### ADD INPUT ###
    next_contact = "" ### TODO ### ADD INPUT ###
    new_add_list = [input_name, phone, email, birthday, last_contact, next_contact]
    cram_write = open(cram_file, "a")
    writer = csv.writer(cram_write)
    writer.writerow(new_add_list)
    cram_write.close()
    print(f"{input_name} added.")


#######################################################################################################
# View Records
#######################################################################################################

# View all records, with sort by
def view_all_with_sort():
    print("")
    print("View Menu:")
    while True:
        for column in cram_columns:
            print(f" {int(cram_columns.index(column)) +1 }. To sort by {column}") # start menu options at 1
        print(" 9. Help\n", "0. Go back")
        sort_by = int(input("> ")) - 1 # convert selection to index
        cram_storage_view.sort_values(cram_columns[sort_by],
                                axis=0,
                                ascending=[True],
                                inplace=True)
        os.system("clear")
        print(f"\nOrdered by {column}:")
        print(cram_storage_view)
        print("\nPress enter to continue ... ")