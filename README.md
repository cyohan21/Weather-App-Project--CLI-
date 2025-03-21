# Python Weather App Project

## Overview

This is simple weather app project, that simulates viewing and adding current weather statistics to cities.

## How It Works

When you launch the program, you will see the following prompt:

> ***Welcome to the weather app! Please enter one of the following:***
>>1: View City
>>
>>2: Add City
>>
>>3: View All Cities
>>
>>4: Exit

If 1 is entered, the program will ask you to enter a city. 
If the city exists in the database, the app will display its temperature, air quality index (AQI), and humidity.
If the city is not found, an error message will be displayed.

If you enter 2, you will be prompted to add a new city:

> Enter the city you would like to add:

If the city already exists in the database, you will receive an error message.
Otherwise, you will be prompted to enter the city's temperature, air quality index, and humidity.
The city will then be successfully added to the database.

If you enter 3, the app will display all stored cities along with their weather data.
If no cities are available, an appropriate message will be displayed.

If you enter 4, the program will close with a farewell message:

> Goodbye!


## Bugs Fixed:

Error handling when viewing a non-existent city.

Preventing duplicate city entries.

Ensuring temperature and AQI inputs are correctly formatted.
