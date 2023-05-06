import pandas as pd
import csv
import os
import time

# import help as help
import shared_variables as shvar

df_temp_clean = "./data_files/cram_storage_temp_clean.csv"
invalid_selection = "That is not an option. Please try again."
# cram_storage_view = pd.read_csv(shvar.cram_storage_file)



shvar.search_sub()
shvar.remove_duplicates()
shvar.display_search()



