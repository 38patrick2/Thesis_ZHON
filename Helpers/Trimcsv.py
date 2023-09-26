import csv
import os

csv_file_path = "path_to_your_csv_file.csv"
temp_file_path = "temp.csv"

# Step 1: Read the CSV file
with open(csv_file_path, 'r', newline='') as csv_file:
    reader = list(csv.reader(csv_file))
    
    # Step 2: Delete the last 9868 elements
    del reader[-9868:]

# Step 3: Save the modified CSV file
with open(temp_file_path, 'w', newline='') as temp_file:
    writer = csv.writer(temp_file)
    writer.writerows(reader)

# Replace the original CSV with the modified one
os.remove(csv_file_path)
os.rename(temp_file_path, csv_file_path)
