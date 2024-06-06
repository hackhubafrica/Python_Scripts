#created by HackHubAfrica
import csv
import json

# Path to the CSV file
csv_file = 'checks.csv'

# Initialize an empty list to store the rows as dictionaries
data_list = []

# Read data from CSV file and populate the list
with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Read each row and convert it to a dictionary
    for row in csvreader:
        data_list.append({key.strip(): value.strip() for key, value in row.items()})

# Convert list of dictionaries to JSON format
json_data = json.dumps(data_list, indent=2)

# Print the JSON data
print(json_data)

# Save to a JSON file
output_file = 'output.json'
with open(output_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(data_list, jsonfile, indent=2)

print(f"JSON data saved to {output_file}")



'''

To handle larger CSV files efficiently, it's better to read and process the file in chunks rather than 
trying to load all the data into memory at once. Here, I will provide an adjusted version of your script 
that reads the CSV file line by line, allowing it to handle larger files more efficiently.

Instead of storing all the data in a single dictionary (
which is suitable for small files), we'll store each row as a dictionary 
and then accumulate these dictionaries in a list.

Explanation

Reading in Chunks: Using csv.DictReader allows us to read the CSV file row by row. Each row is read as an OrderedDict.
Appending to a List: Instead of creating a single dictionary for headers and values, each row is converted to a dictionary and added to a list. This approach is more memory efficient when dealing with large files.
Convert and Save: The list of dictionaries is converted to JSON format and saved to a file.

This script should handle larger CSV files more effectively by avoiding the need to load the entire file into memory at once.
'''
