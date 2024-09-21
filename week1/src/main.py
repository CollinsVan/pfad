# import dotenv
import os
import datetime
import csv

# Load environment variables
# dotenv.load_dotenv()

file = 'C:/Users/CollinsVan/my-forked-repo/data.csv'

# Automatically identify valid rows (call this after actually reading the CSV file)
def is_data_row(row):
    try:
        # Check if columns 0, 1, and 2 are numeric
        return (row[0].strip().isdigit() and row[1].strip().isdigit() and row[2].strip().isdigit())
    except IndexError:
        return False

# Check if the file exists
if os.path.exists(file):
    with open(file, 'r', encoding='UTF8') as f:
        reader = csv.reader(f)

        for row in reader:
            # Filter valid rows
            if is_data_row(row):
                columns = [column.strip() for column in row]
                row_string = " ".join(columns).strip()
                if row_string == "":
                    continue 
                print(f'{row_string}')

                year = int(columns[0])
                month = int(columns[1])
                day = int(columns[2])
                value = columns[3]
                dc = columns[4]

                # If the value is 'Trace', treat it as 0.0
                if value == 'Trace':
                    value = 0.0
                else:
                    value = float(value)

                    # Generate a datetime object
                    dt = datetime.datetime(year, month, day)
                    
                    # If dc is 'C', print the result; otherwise, skip
                    if dc == 'C':
                        print(f'{dt} - {value}')

else:
    print("CSV_FILE 不存在")