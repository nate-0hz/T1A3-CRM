# 345678901234567890123456789012345678901234567890123456789012345678900123456789
import pandas as pd
import time
import menu_modules.help as help
import menu_modules.shared_variables as shvar

# handles file not found for cram_storage_file
try:
    cram_storage_view = pd.read_csv(shvar.cram_storage_file)
except FileNotFoundError:
    pass

################################################################################
# Search sequence
################################################################################

# function to display search results from temp csv file
def display_search():
    # Read clean temp file
    df = pd.read_csv(shvar.df_temp_clean)
    if df.empty == False:
        print(df)
        input("Press enter to continue ... ")
        shvar.clear_terminal()
    else:
        print("No matches found.")

def execute_search():
    shvar.clear_temp()
    shvar.search_sub()
    shvar.remove_duplicates()
    shvar.display_search()

################################################################################
# Display Records sequence
################################################################################

def view_all_with_sort():
    cram_storage_view = pd.read_csv(shvar.cram_storage_file)
    shvar.clear_terminal()
    for column in shvar.cram_columns:
        print(f" {int(shvar.cram_columns.index(column)) +1 }. To sort by {column}")
            # start menu options at 1
    print(" 9. Help\n", "0. Go back")
    
    # catch non-integer input
    try:
        sort_by = int(input("> ")) - 1 # subtract 1 to align with index
    except ValueError:
        print(f"\n{shvar.invalid_selection}\n")
        time.sleep(1)
        return
    # takes menu input to progress flow. Option logic is below
    if 0 <= (sort_by) <= 7:
        cram_storage_view.sort_values(shvar.cram_columns[sort_by],
                                axis=0,
                                ascending=[True],
                                inplace=True)
        shvar.clear_terminal()
        pd.options.display.max_rows = None
        pd.options.display.width = None
        print(cram_storage_view)
        print(f"\n{len(cram_storage_view)} records, ordered by "
            f"{shvar.cram_columns[sort_by]}.")
        input("\nPress enter to continue ... ")
    elif (sort_by) == 8:
        shvar.clear_terminal()
        help.view_all_help.display_help()
        input("\nPress enter to continue ... ")
        shvar.clear_terminal()
    elif sort_by == -1:
        return
    else:
        print(f"\n{shvar.invalid_selection}\n")
        # time.sleep(1)

################################################################################
# View Records Sub-Menu
################################################################################

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
        print(f"\n{shvar.invalid_selection}\n")
        time.sleep(1)

def action_view_menu(menu_selection):
    shvar.clear_terminal()
    if menu_selection == view_menu_options[0]: # View all
        view_all_with_sort()
    elif menu_selection == view_menu_options[1]: # Search
        print("Search contacts.")
        execute_search()
    elif menu_selection == view_menu_options[2]: # Help
        shvar.clear_terminal()
        help.view_menu_help.display_help()
        input("\nPress enter to continue ... ")
        shvar.clear_terminal()
    elif menu_selection == view_menu_options[3]: # Go back
        print()
    else:
        print(f"\n{shvar.invalid_selection}\n")
        time.sleep(1)

################################################################################
# View Menu Flow
################################################################################


def view_flow():
    menu_selection = ""
    while menu_selection != "0":
        shvar.clear_terminal()
        menu_selection = view_menu_selection()
        action_view_menu(menu_selection)
    return
            
        