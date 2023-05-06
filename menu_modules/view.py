import pandas as pd
import csv
import os
import time

import menu_modules.help as help
import menu_modules.shared_variables as shvar



df_temp = "./data_files/cram_storage_temp.csv"
df_temp_clean = "./data_files/cram_storage_temp_clean.csv"
invalid_selection = "That is not an option. Please try again."


def clear_terminal(): 
    os.system("clear")


#######################################################################################################
# Search sequence
#######################################################################################################

# function to clear temp csv file
def clear_temp():
    with open(df_temp, "w") as f:
        writer = csv.writer(f)
        writer.writerow(shvar.cram_columns)
        f.close()

# function to search for sub-string in csv file and add rows to temp csv file
def search_sub():
    search = input("Type what you would like to search for: ")
    # Clear temp file
    clear_temp()
    # Read storage file
    with open(shvar.cram_storage_file, "r") as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            for i in row:
                if i.find(search) != -1 or i.find(search.capitalize()) != -1 or i.find(search.lower()) != -1 or i.find(search.upper()) != -1:
                    with open(df_temp, "a") as file_temp:
                        writer = csv.writer(file_temp)
                        writer.writerow(row)
                else:
                    pass ### revisit this ###

# function to remove duplicates from temp csv file
def remove_duplicates():
    # Read temp file
    df = pd.read_csv(df_temp, sep=",")
    df.drop_duplicates(subset=None, keep="first", inplace=True)
    # Write to clean temp file
    df.to_csv(df_temp_clean, index=False)

# function to display search results from temp csv file
def display_search():
    # Read clean temp file
    df = pd.read_csv(df_temp_clean)
    if df.empty == False:
        print(df)
        input("Press enter to continue ... ")
        clear_terminal()
    else:
        print("No matches found.")

def execute_search():
    clear_temp()
    search_sub()
    remove_duplicates()
    display_search()

#######################################################################################################
# Display Records sequence
#######################################################################################################

def view_all_with_sort():
    cram_storage_view = pd.read_csv(shvar.cram_storage_file)
    clear_terminal()
    for column in shvar.cram_columns:
        print(f" {int(shvar.cram_columns.index(column)) +1 }. To sort by {column}") # start menu options at 1
    print(" 9. Help\n", "0. Go back")
    sort_by = int(input("> ")) - 1 # subtract 1 to align with index
    if 0 <= (sort_by) <= 7:
        shvar.cram_storage_view.sort_values(shvar.cram_columns[sort_by],
                                axis=0,
                                ascending=[True],
                                inplace=True)
        clear_terminal()
        pd.options.display.max_rows = None
        pd.options.display.width = None
        print(cram_storage_view)
        print(f"\n{len(cram_storage_view)} records, ordered by {shvar.cram_columns[sort_by]}.")
        input("\nPress enter to continue ... ")
    elif (sort_by) == 8:
        clear_terminal()
        help.view_all_help.display_help()
        input("\nPress enter to continue ... ")
        clear_terminal()
    elif sort_by == -1:
        return
    else:
        print(f"\n{invalid_selection}\n")
        time.sleep(1)

#######################################################################################################
# View Records Sub-Menu
#######################################################################################################

view_menu = { "1": "View all Contacts",
              "2": "Search Contacts",
              "9": "Help",
              "0": "Go Back",
             }

view_menu_options = list(view_menu.keys())

def view_menu_selection():
    print(f"View Contacts:")
    for item in view_menu:
        print(f"{item}. {view_menu.get(item)}")
    view_selection = input("> ")
    if view_selection in view_menu_options:
        return(view_selection)
    else:
        print(f"\n{invalid_selection}\n")
        time.sleep(1)

def action_view_menu(menu_selection):
    clear_terminal()
    if menu_selection == view_menu_options[0]: # View all
        view_all_with_sort()
    elif menu_selection == view_menu_options[1]: # Search
        print("Search contacts.")
        execute_search()
    elif menu_selection == view_menu_options[2]: # Help
        clear_terminal()
        help.view_menu_help.display_help()
        input("\nPress enter to continue ... ")
        clear_terminal()
    elif menu_selection == view_menu_options[3]: # Go back
        print()
    else:
        print(f"\n{invalid_selection}\n")
        time.sleep(1)

#######################################################################################################
# View Menu Flow
#######################################################################################################

def view_flow():
    menu_selection = ""
    while menu_selection != "0":
        clear_terminal()
        menu_selection = view_menu_selection()
        action_view_menu(menu_selection)
    return
            
        