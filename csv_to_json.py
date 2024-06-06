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
