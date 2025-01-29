import csv
import json

# Read the CSV file
with open('', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Convert CSV data to a list of dictionaries
    data = list(csv_reader)

# Write the data to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)