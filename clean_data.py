import pandas as pd
import json

# Load CSV data
df = pd.read_csv('C:/Projects/SearchAdminPanel/restaurants_small.csv')

# Function to clean price fields
def clean_price(price):
    # Remove non-numeric characters and convert to float
    try:
        return float(price.split()[0].replace(',', ''))
    except ValueError:
        return None

# Parse and clean the items JSON field
for index, row in df.iterrows():
    items = json.loads(row['items'])
    cleaned_items = {}
    for dish_name, price in items.items():
        cleaned_price = clean_price(price)
        if cleaned_price is not None:
            cleaned_items[dish_name] = cleaned_price
    df.at[index, 'items'] = json.dumps(cleaned_items)

# Save cleaned CSV
df.to_csv('C:/Projects/SearchAdminPanel/restaurants_small.csv', index=False)
print("CSV cleaned and saved successfully!")

import pandas as pd
import json

# Load CSV data
df = pd.read_csv('C:/Projects/SearchAdminPanel/restaurants_small.csv')

# Function to clean price fields
def clean_price(price):
    # Remove non-numeric characters and convert to float
    try:
        return float(str(price).split()[0].replace(',', ''))
    except ValueError:
        return None

# Parse and clean the items JSON field
for index, row in df.iterrows():
    items = json.loads(row['items'])
    cleaned_items = {}
    for dish_name, price in items.items():
        cleaned_price = clean_price(price)
        if cleaned_price is not None:
            cleaned_items[dish_name] = cleaned_price
    df.at[index, 'items'] = json.dumps(cleaned_items)

# Ensure full_details is a string
df['full_details'] = df['full_details'].apply(lambda x: json.dumps(x) if not isinstance(x, str) else x)

# Save cleaned CSV
df.to_csv('C:/Projects/SearchAdminPanel/restaurants_small.csv', index=False)
print("CSV cleaned and saved successfully! 2")
