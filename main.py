# Importing libraries

import datetime as dt
import requests
import csv
import random

# API

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

API_KEY = "Insert your API KEY"
CITY = "Zaragoza"
name = "Name"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

# Celsius from Kelvin function

def kelvin_to_celsius(kelvin):
    celsius = kelvin -273.15
    return celsius

# Getting the info we need from the Weather Response

response = requests.get(url).json()

main = response["weather"][0]["main"]

temp_kelvin = response["main"]["temp"]
temp_celsius = round(kelvin_to_celsius(temp_kelvin))

# List of weather conditions: https://openweathermap.org/weather-conditions: Thunderstorm, Drizzle, Rain, Snow, Clear, Clouds

# Initialize an empty dictionary to store clothing data
clothes_data = []

# Open the CSV file and read data into the dictionary
with open('sergioolles_clothes.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        clothes_data.append(row)

# Create empty variables
selected_top = None
selected_overtop = None
selected_coat = None
selected_bottom = None
selected_shoe = None

# Initialize lists to store clothing categories
tops_eligibles = []
overtops_eligibles = []
coats_eligibles = []
bottoms_eligibles = []
shoes_eligibles = []

# Open the CSV file and read data into the lists
with open('sergioolles_clothes.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row['Category'].strip().lower()
        rain_protection = int(row['Rain protection'])
        heat_coefficient = int(row['Heat Coefficient'])

        # Always add tops
        if category == 'top':
            tops_eligibles.append(row['Name'])
        
        # Add overtops depending on the temperature (always below 22º)
        elif category == 'overtop':
            if 10 <= temp_celsius <= 22:
                if 3 < heat_coefficient < 7:
                    overtops_eligibles.append(row['Name'])
            elif temp_celsius < 10:
                if heat_coefficient >= 7:
                    overtops_eligibles.append(row['Name'])
        
        # Add bottoms depending on the temperature
        elif category == 'bottom':
            if temp_celsius > 22:
                if heat_coefficient <= 3:
                    bottoms_eligibles.append(row['Name'])
            elif 10 <= temp_celsius <= 22:
                if 3 < heat_coefficient <= 7:
                    bottoms_eligibles.append(row['Name'])
            elif temp_celsius < 10:
                if heat_coefficient > 7:
                    bottoms_eligibles.append(row['Name'])

        # Add coats if temperature is below 10º
        elif category == 'coat':
            if temp_celsius < 10:
                if heat_coefficient > 7:
                    coats_eligibles.append(row['Name'])

        # Add shoes depending on temperature
        elif category == 'shoes':
            if temp_celsius > 22:
                if heat_coefficient <= 3:
                    shoes_eligibles.append(row['Name'])
            elif 10 <= temp_celsius <= 22:
                if 3 < heat_coefficient <= 7:
                    shoes_eligibles.append(row['Name'])
            elif temp_celsius < 10:
                if heat_coefficient > 7:
                    shoes_eligibles.append(row['Name'])


# Check if the weather requires rain_protection items
if main in ["Thunderstorm", "Drizzle", "Rain", "Snow"]:

    # Filter eligible bottoms with rain protection
    bottoms_eligibles = [bottom for bottom in bottoms_eligibles if rain_protection == 1]

    # Filter eligible shoes with rain protection
    shoes_eligibles = [shoe for shoe in shoes_eligibles if rain_protection == 1]

# Select one top randomly
if tops_eligibles:
    selected_top = random.choice(tops_eligibles)
else:
    print("No tops found. Please add some.")

# Select one overtop randomly
if overtops_eligibles:
    selected_overtop = random.choice(overtops_eligibles)
else:
    print("No overtops found. Please add some.")

# Select one coat randomly
if coats_eligibles:
    selected_coat = random.choice(coats_eligibles)
else:
    print("No coats found. Please add some.")

# Select one bottom randomly
if bottoms_eligibles:
    selected_bottom = random.choice(bottoms_eligibles)
else:
    print("No bottoms found. Please add some.")

# Select shoes randomly
if shoes_eligibles:
    selected_shoe = random.choice(shoes_eligibles)
else:
    print("No shoes found. Please add some.")

# Print the outfit (top, bottom, shoes) recommendation
print("Hello, {}. Based on the weather today in {} ({} and currently {}º), you could wear the {} with the {} and your {}.".format(name, CITY, main.lower(), temp_celsius, selected_top.lower(), selected_bottom.lower(), selected_shoe.lower()))

# Add overtop if weather requires it
if overtops_eligibles:
    print("In adition to that, you can wear your {}.".format(selected_overtop.lower()))

# Add coat if weather requires it
if coats_eligibles:
    print("To protect yourself from the cold, you can wear your {}.".format(selected_coat.lower()))