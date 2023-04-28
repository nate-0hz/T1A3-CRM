# 345678901234567890123456789012345678901234567890123456789012345678900123456789

# import add_record
import menu_modules.MainMenu as main

#import keyboard for hotkey use
import keyboard

cram_storage = "cram-storage.csv"

def file_check():
    try:
        readmeFile = open(cram_storage, "r")
    except FileNotFoundError as err:
        print("""
            You do not have a database for CRaM. 
            Would you like to create one now?
            (Yes/No)
            """)

file_check()
menu_selection = main.main_menu_selection()
main.action_main_menu(menu_selection)
