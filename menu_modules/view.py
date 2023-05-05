import pandas as pd
import csv
import os
import time

df_temp = "../cram_storage_temp.csv"
df_temp_clean = "../cram_storage_temp_clean.csv"
cram_columns = ["fname", "lname", "phone", "company", "email", "birthday", "last_contact", "next_contact"]
cram_storage_file = "cram_storage3.csv" ### change to cram storage
cram_storage_view = pd.read_csv(cram_storage_file)
invalid_selection = "That is not an option. Please try again."

############
# Search sequence
############

# function to clear temp csv file
def clear_temp():
    with open(df_temp, "w") as f:
        writer = csv.writer(f)
        writer.writerow(cram_columns)
        f.close()

# function to search for sub-string in csv file and add rows to temp csv file
def search_sub():
    search = input("Type what you would like to search for: ")
    # Clear temp file
    clear_temp()
    # Read storage file
    with open(cram_storage_file, "r") as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            for i in row:
                if i.find(search) != -1 or i.find(search.capitalize()) != -1 or i.find(search.lower()) != -1 or i.find(search.upper()) != -1:
                    with open(df_temp, "a") as file_temp:
                        writer = csv.writer(file_temp)
                        writer.writerow(row)
                else:
                    break

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
    else:
        print("No matches found.")

def execute_search():
    clear_temp()
    search_sub()
    remove_duplicates()
    display_search()

############
# Display Records sequence
############

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

############
# View Records Sub-Menu
############

view_menu = { "1": "View all Contacts",
              "2": "Search Contacts",
              "9": "Help",
              "0": "Quit CRaM",
             }

view_menu_options = list(view_menu.keys())

    # search = input("What search: ")
    # clear_temp()
    # search_sub()
    # remove_duplicates()
    # display_search()


def view_menu_selection():
    while True:
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
    if menu_selection == view_menu_options[0]: # View all
        print("View all contacts.")
        view_all_with_sort()
        # break
    elif menu_selection == view_menu_options[1]: # Search
        print("Search contacts.")
        execute_search()
        # break
    elif menu_selection == view_menu_options[2]: # Help
        print(f"help") # test
        # break
    elif menu_selection == main_menu_options[3]: # Go back
        return
        # help.MainMenuHelp()
        # break
    # elif menu_selection == main_menu_options[4]: # Quit
    #     os.system("clear")
    #     print(f"Thanks for using CRaM.")
    #     sys.exit()

############
# View Menu Flow
############

def view_flow():
    while True:
        menu_selection = view_menu_selection()
        action_view_menu(menu_selection)