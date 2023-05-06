import pandas as pd
import os
import csv
import sys


cram_storage_file = "../data_files/cram_storage.csv"
df_temp = "../data_files/cram_storage_temp.csv"
df_temp_clean = "../data_files/cram_storage_temp_clean.csv"


# main menu dict
main_menu = { "1": "View Contacts",
              "2": "Add Contacts",
              "3": "Edit Contacts",
              "9": "Help",
              "0": "Quit CRaM",
             }


cram_columns = ["first_name", "last_name", "phone", "company", "email", "birthday", "last_contact", "next_contact"]
main_menu_options = list(main_menu.keys())

# # passing over FileNotFoundError as if cram_storage_file does not exist, it will be created in file_check()
# try:
#     cram_storage_read = open(cram_storage_file, "r")
# except FileNotFoundError:
#     pass

# # try:
# #     cram_storage_append = open(cram_storage_file, "a")
# # except FileNotFoundError:
# #     pass

# # try:
# #     cram_storage_write = open(cram_storage_file, "w")
# # except FileNotFoundError:
# #     pass

# # also passes FileNotFoundError, along with Attribute and empty data error
# try:
#     cram_storage_view = pd.read_csv(cram_storage_file)
# except FileNotFoundError:
#     pass
# except AttributeError:
#     pass
# except pd.errors.EmptyDataError:
#     pass

def clear_terminal(): 
    os.system("clear")

# function to clear temp csv file
def clear_temp():
    with open(df_temp, "w") as f:
        writer = csv.writer(f)
        writer.writerow(cram_columns)
        f.close()
    

def file_check():
    try:
        with open(cram_storage_file, "r") as f:
            f.close()
    except FileNotFoundError:
        print("Created cram_storage.csv")
        with open("./data_files/cram_storage.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(cram_columns) ### Revisit this ###
            # f.close()
    finally:
        return

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

# function to remove duplicates from temp csv file and write to clean temp csv file
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
        return df
    else:
        print("No matches found.")