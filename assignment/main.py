# import dotenv
import os
import csv
import numpy as np
import matplotlib.pyplot as plt

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

        max_month = 0
        max_day_in_each_month = {}
        
        # First pass through the file to find the maximum month and the maximum number of days in each month
        for row in reader:
            # Filter valid rows
            if is_data_row(row):
                columns = [column.strip() for column in row]
                
                month = int(columns[1])
                day = int(columns[2])
                max_month = max(max_month, month)
                if month not in max_day_in_each_month:
                    max_day_in_each_month[month] = day
                else:
                    max_day_in_each_month[month] = max(max_day_in_each_month[month], day)

        # Find the maximum number of days across all months
        max_days = max(max_day_in_each_month.values())
        # Handle irregular days (different number of months, different number of days), ensure the array size is large enough
        value_2d = np.zeros((max_month, max_days))

        # Re-pass through the file to populate the data
        f.seek(0)
        for row in reader:
                if is_data_row(row):
                    columns = [column.strip() for column in row]
                    month = int(columns[1])
                    day = int(columns[2])
                    value = columns[3]
                    dc = columns[4]
                    
                    # If the value is 'Trace', treat it as 0.0
                    if value == 'Trace':
                        value = 0.0
                    else:
                        value = float(value)
                    
                    if dc == 'C':
                        # Fill the rainfall data into the 2D array
                        value_2d[month - 1, day - 1] = value
                    
        # Create the X and Y coordinates
        x = np.arange(1, max_month + 1)
        y = np.arange(1, max_days + 1)


        # Use pcolormesh to plot the data
        pcm = plt.pcolormesh(x, y, value_2d.T, cmap='Blues', shading='auto', vmin=0, vmax=np.max(value_2d))

        # Add a color bar
        plt.colorbar(pcm, label='Rainfall (mm)')

        # Add labels and title
        plt.title('2024')
        plt.xlabel('Month')
        plt.ylabel('Day')

        # Display the plot
        plt.show()

else:
    print("CSV_FILE does not exist")