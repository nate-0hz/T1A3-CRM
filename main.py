# 345678901234567890123456789012345678901234567890123456789012345678900123456789
import os
# from help import main_menu_help

main_menu = { "1": "View Contacts",
              "2": "Add Contacts",
              "3": "Edit Contacts",
              "0": "Help",
              "Q": "Quit CRaM",
             }

VALID_MAIN_MENU_OPTIONS = ("1", "2", "3", "0", "Q")
project_name = "CRaM"
project_welcome = "Welcome to CRaM, the best CRM in 2023."
project_underline = 12 * "="
project_menu_instruction = "What would you like to do?"

main_menu_selection = ""
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
    print(f"{project_menu_instruction}")
    for item in main_menu:
        print(f"{item}. {main_menu.get(item)}")
    main_menu_selection = input("> ")
    return main_menu_selection


welcome()
print(main_menu_selection)
