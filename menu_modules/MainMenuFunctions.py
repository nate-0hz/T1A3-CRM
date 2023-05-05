# import os to clear terminal, import sys for a clean exit, 
# import time for sleep, import keyboard for hotkey use
import os
import time
import csv
import sys
import pandas as pd

# importing created modules
# import classes.class_record as record





#######################################################################################################
# View Records
#######################################################################################################

# View all records, with sort by
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