import pandas as pd
import csv
import os
import time

# import help as help
import shared_variables as shvar

editing_dict = {}
invalid_selection = "That is not an option. Please try again."
# cram_storage_view = pd.read_csv(shvar.cram_storage_file)

def edit_list(results_list):
    index = int(input("Select the index number of the record to edit: "))
    print(results_list[index])
    print(index)

# create dictionary from keys and element returned by user

    return editing_dict, index

# function to display search results from temp csv file
def edit_display_search():
    # Read clean temp file
    df = pd.read_csv(shvar.df_temp_clean)
    if df.empty == False:
        print(df)
        return df
    else:
        print("No matches found.")

# present record to edit
def edit_record(editing_list, index):
    pass









#######################################################################################################
# Reuses search code in view.py, saved in shared_variables.py
#######################################################################################################

shvar.search_sub()
shvar.remove_duplicates()
results = edit_display_search()
print(results)
results_list = results.values.tolist()
editing_dict = edit_list(results_list)
