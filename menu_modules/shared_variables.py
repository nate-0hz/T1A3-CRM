# 345678901234567890123456789012345678901234567890123456789012345678900123456789
import pandas as pd
import os
import csv
import time

cram_storage_file = "./data_files/cram_storage.csv"
df_temp = "./data_files/cram_storage_temp.csv"
df_temp_clean = "./data_files/cram_storage_temp_clean.csv"
invalid_selection = "That is not an option. Please try again."
cram_columns = ["first_name", "last_name", "phone", "company", "email",
    "birthday", "last_contact", "next_contact"]

project_name = "CRaM 2023"

# Creates standard centred underline
def underline_centre():
    project_underline = 12 * "="
    print(f"{project_underline.center(80)}\n")

def welcome(page):
    underline_centre()
    print(f"{page(80)}\n")
    underline_centre()

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
            writer.writerow(cram_columns)
            # f.close()
    finally:
        return

# function to search for sub-string in csv file and add rows to temp csv
def search_sub():
    search = input("Type text to search for: ")
    # Clear temp file
    clear_temp()
    # Read storage file
    with open(cram_storage_file, "r") as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            for i in row:
                if i.find(search) != -1 or i.find(search.capitalize()) != -1 or \
                    i.find(search.lower()) != -1 or i.find(search.upper()) != -1:
                    with open(df_temp, "a") as file_temp:
                        writer = csv.writer(file_temp)
                        writer.writerow(row)

# function to remove duplicates from temp csv file and write to clean temp csv
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
        print("No matches found. Returning to View Menu")
        time.sleep(1)