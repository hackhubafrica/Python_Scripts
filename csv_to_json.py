import csv
import json

# Path to the CSV file
csv_file = 'wappalyzer_freelancer-htb.csv'

# Initialize an empty dictionary to store the information
info_dict = {}

# Read data from CSV file and populate the dictionary
with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)  # Read the headers
    values = next(csvreader)   # Read the values
    
    # Populate the dictionary with headers and values
    for idx, header in enumerate(headers):
        info_dict[header.strip()] = values[idx].strip()

# Convert dictionary to JSON format
json_data = json.dumps(info_dict, indent=2)

# Print the JSON data
#print(json_data)

# Save to a JSON file
output_file = 'output.json'
with open(output_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(info_dict, jsonfile, indent=2)

print(f"JSON data saved to {output_file}")
