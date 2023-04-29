# 345678901234567890123456789012345678901234567890123456789012345678900123456789

# import local modules
import menu_modules.MainMenu as main
import menu_modules.help as help

# import csv for csv file handling, import keyboard for hotkey use
# import sys for clean exit, import os to clear terminal
import csv
import sys
import os

#######################################################################################################
# Main menu flow
#######################################################################################################

cram_file = "cram_storage.csv"
run_loop = True

# checks if cram_storage.csv exists
def file_check():
    try:
        cram_storage = open(cram_file, "r")
        cram_storage.close()
    except FileNotFoundError:
        os.system("clear")
        print("You do not have a database for CRaM.")
        create_storage = input("Would you like to create one now? (y/n): ")
        if create_storage == "y":
            cram_storage = open(cram_file, "w")
            cram_storage.write(f"name,phone,company,email,birthday,last_contact,next_contact\n")
            cram_storage.close()
        else:
            os.system("clear")
            print("CRaM cannot continue without a database.")
            sys.exit()

# actions main menu input
def action_main_menu(menu_selection):
    while True:
        if menu_selection == main.menu_options[0]: # view contacts
            print(f"action_main_menu: {menu_selection}") # test
            break
        elif menu_selection == main.menu_options[1]: # add contacts
            print("Add a contact.")
            add_entry()
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



def add_entry():
    input_name = input("What is the name to add? (leave blank and press return to exit) ")
    while input_name == "":
        break
    else:
        cram_storage = open(cram_file, "r") # open file
        with cram_storage as open_file:
            doesExist = open_file.read()
            cram_storage.close()
            print(f"after reading: {cram_storage}")
            if input_name in doesExist:
                add_new = input(f"{input_name} already exists. Create new entry?(yes/no) ")
                if add_new == "yes":
                    gather_details(input_name)
                    # add_another()
                else:
                    # run_loop = False
                    print("new entry not breaking")
                    # return run_loop
            else:
                gather_details(input_name)
                # add_another()

def gather_details(input_name):
    phone = input("Add phone number: ")
    email = input("Add email: ")
    birthday = ""
    last_contact = ""
    next_contact = ""
    new_add_list = [input_name, phone, email, birthday, last_contact, next_contact]
    cram_write = open(cram_file, "a") # open file
    writer = csv.writer(cram_write)
    writer.writerow(new_add_list)
    cram_write.close() # close file confirmed
    print(f"after writing: {cram_write.mode}")
    print
    return

# def add_another():  ### TO DO ### FIX ADD ANOTHER LOOP
#     more = input("Add another?(yes/no) ")
#     while more not in ["yes"]:
#         break



#######################################################################################################
# Flow control
#######################################################################################################

def main_flow():
    while True:
        menu_selection = main.main_menu_selection()
        action_main_menu(menu_selection)

file_check()
main_flow()
