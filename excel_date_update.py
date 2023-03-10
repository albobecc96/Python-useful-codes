import pandas as pd
import datetime

# Get today's date
today_date = datetime.datetime.today().strftime('%Y-%m-%d')

# Filepath and filename with today's date
file_path = "path/to/excel/fil/"
file_name = "data_{}.xlsx".format(today_date)

# Read Excel file into pandas dataframe
df = pd.read_excel(file_path + file_name)

# Do something with the data in the dataframe
# ...

# Save changes back to the Excel file
df.to_excel(file_path + file_name, index=False)