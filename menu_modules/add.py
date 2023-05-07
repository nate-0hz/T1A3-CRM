# 345678901234567890123456789012345678901234567890123456789012345678900123456789
import csv
import time
import dateutil.parser

import menu_modules.shared_variables as shvar

################################################################################
# Functions used to add entry
################################################################################

# Add a new entry and check if entry exists
def add_entry():
    run_loop = True
    while run_loop == True:
        first_name = input("What is the first name of the person to add? "
                           "(Type 'exit' to go back) ")
        if first_name == "exit":
            run_loop = False
            return run_loop
        else:
            last_name = input("What is the last name? ")
            with open(shvar.cram_storage_file, "r") as open_file:
                doesExist = open_file.read()
                if first_name and last_name in doesExist:
                    add_new = input(f"{first_name} {last_name} already exists. "
                                    "Create new entry?(yes/no) ")
                    if add_new == "yes":
                        gather_details(first_name, last_name)
                        # add_another()
                    elif add_new == "no":
                        return
                    else:
                        print("Invalid input. Starting again.")
                        time.sleep(1)
                        continue
                else:
                    gather_details(first_name, last_name)
                    # add_another()
    
    open(shvar.cram_storage_file, "r").close()
    return

# Gather the details to add
def gather_details(first_name, last_name):
    cram_storage_append = open(shvar.cram_storage_file, "a")
    phone = input("Add phone number: ")
    company = input("Add company: ")
    email = input("Add email: ")

    print("Add birthday.", end=" ")
    birthday = check_valid_date_100()

    print("Add date you last contacted them.", end=" ")
    last_contact = check_valid_date_100()

    print("Add date you want to contact them again.", end=" ")
    next_contact = check_valid_date_100()

    new_add_list = [first_name, last_name, phone, company, email, birthday, 
                    last_contact, next_contact]
    print("Contact added.")
    writer = csv.writer(cram_storage_append)
    writer.writerow(new_add_list)
    cram_storage_append.close()

def check_valid_date_100():
    attempts = 0
    # checks date formatting
    while True:
        try:
            date = input("Add date (dd/mm/yy): ")
            dateutil.parser.parse(date,
                parserinfo=dateutil.parser.parserinfo(dayfirst=True))
            return date
        except ValueError:
            attempts += 1
            if attempts >= 3:
                print("Maximum attempts reached.")
                raise
            print("Not a valid date. Please try again.")

# Add another entry
def add_another():
    more = input("Add another?(yes/no): ")
    if more != "yes":
        return
            
################################################################################
# Add entry flow
################################################################################


def add_flow():
    add_entry()
    return

