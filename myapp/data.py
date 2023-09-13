import json

# Specify the relative file path to the JSON file (inside the same directory as data.py)
file_path = 'priohub.json'

# Open and load the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Assuming "priohub.json" contains a list of items
items = data['items']

# Loop through the items and extract information
for item in items:
    item_id = item['id']
    item_name = item['name']
    
    print(f"Item ID: {item_id}, Item Name: {item_name}")
