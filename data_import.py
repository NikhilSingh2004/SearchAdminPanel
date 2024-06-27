import json
import pandas as pd
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search.settings')
django.setup()

from core.models import Restaurant, Dish

# Load cleaned CSV data
df = pd.read_csv('C:/Projects/SearchAdminPanel/restaurants_small.csv')

def parse_full_details(full_details):
    if pd.isna(full_details):
        return {}
    try:
        return json.loads(full_details)
    except (TypeError, json.JSONDecodeError):
        return {}

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Create or get the Restaurant object
    restaurant, created = Restaurant.objects.get_or_create(
        name=row['name'],
        location=row['location'],
        lat_long=row['lat_long'],
        defaults={'full_details': parse_full_details(row['full_details'])}
    )

    # Parse the cleaned items JSON and create Dish objects
    items = json.loads(row['items'])
    for dish_name, price in items.items():
        try:
            price = float(str(price).split()[0].replace(',', ''))
        except ValueError:
            continue
        Dish.objects.create(
            name=dish_name,
            price=price,
            restaurant=restaurant
        )

    print(f"{index + 1} Rows Done")

print("Data import completed successfully!")
