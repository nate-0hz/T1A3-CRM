import pandas as pd
import os
import csv
import sys


cram_storage_file = "./data_files/cram_storage.csv"

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
