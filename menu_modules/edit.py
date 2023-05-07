# 345678901234567890123456789012345678901234567890123456789012345678900123456789
import pandas as pd
import time
import menu_modules.shared_variables as shvar

editing_dict = {}
invalid_selection = "That is not an option. Please try again."

# function to display search results from temp csv file
def edit_display_search():
    # Read clean temp file
    df = pd.read_csv(shvar.df_temp_clean)
    if df.empty == False:
        print(df)
        return df
    else:
        print("No matches found.")

# Select the record from cram_storage_file to edit
def edit_list(results_list):
    try:
        index = int(input("Select the index number of the record to edit: "))
    except ValueError:
        print(invalid_selection)
        time.sleep(1)
        return
    except IndexError:
        print(invalid_selection)
        time.sleep(1)
        return
    if index in range(len(results_list)):
        chosen_record = results_list[index]
        return chosen_record
    else:
        return

#make a dictionary from the list to display, assisting the user in updating
def make_dict(chosen_record):
    # create dictionary from keys and element returned by user
    try:
        editing_dict = dict(zip(shvar.cram_columns, chosen_record))
    except TypeError:
        print("Invalid selection. Returning to Main Menu.")
        time.sleep(1)
        return
    return editing_dict

# takes the updates in a temp list, then updates the csv.
def edit_record(editing_dict, chosen_record):
    # present record to edit
    temp_list = []
    i = 0
    try:
        for key in editing_dict:
            value = input(f"Current {key} is {editing_dict[key]}. "
                        "New value (or press enter to keep): ")
            if value == "":
                temp_list.insert(i, chosen_record[i])
            else:
                temp_list.insert(i, value)
            i += 1
    except TypeError:
        print("Invalid selection. Returning to Main Menu.")
        time.sleep(1)
        return

    # find and update record in cram_storage_file
    df = pd.read_csv(shvar.cram_storage_file)
    mask = (df['first_name'] == chosen_record[0]) & (df['last_name'] == chosen_record[1]) \
        & (df['phone'] == chosen_record[2]) & (df['company'] == chosen_record[3]) \
        & (df['email'] == chosen_record[4]) & (df['birthday'] == chosen_record[5]) \
        & (df['last_contact'] == chosen_record[6]) \
        & (df['next_contact'] == chosen_record[7])
    df.loc[mask] = temp_list
    df.to_csv(shvar.cram_storage_file, index=False)
    print("\nRecord updated. Returning to Main Menu.")
    time.sleep(1)

################################################################################
# Edit Flow
################################################################################


def edit_flow():
    shvar.clear_terminal()
    print("Edit a contact.\n")
    shvar.search_sub()
    shvar.remove_duplicates()
    results = edit_display_search()
    try:
        results_list = results.values.tolist()
    except AttributeError:
        print("Attribute error. Result not found. Returning to Main Menu.")
        time.sleep(1)
        return
    except TypeError:
        print("Type error. Result not found. Returning to Main Menu.")
        time.sleep(1)
        return
    chosen_record = edit_list(results_list)
    editing_dict = make_dict(chosen_record)
    edit_record(editing_dict, chosen_record)

