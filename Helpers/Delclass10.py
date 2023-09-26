import csv
import os

csv_file_path = "E:\\University\\ZHON\\Jup\\Dataset\\train_dir\\train_dir\\trainLabels.csv"
class_dir = "E:\\University\\ZHON\\Jup\\Dataset\\train_dir\\train_dir\\class_2"

# Read the resulting CSV file and get names of class 10
names_in_csv_class = []
with open(csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # skip the header
    for row in reader:
        name, class_num = row
        if int(class_num) == 2:
            names_in_csv_class.append(name.strip('"'))

# Delete the files from class that are not in the CSV file
for file_name in os.listdir(class_dir):
    # Remove the .png extension from the filename for comparison
    name_without_extension = os.path.splitext(file_name)[0]
    
    if name_without_extension not in names_in_csv_class:
        file_path = os.path.join(class_dir, file_name)
        os.remove(file_path)
