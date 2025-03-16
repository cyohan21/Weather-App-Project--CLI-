class WeatherDatabase: # Change name to database as the app will be a new class.
    weather_dict = {
        'Ottawa': {'Temperature': '12*C', 'Air Quality Index': 4, 'Humidity': '80%'},
        'Montreal':{'Temperature': '15*C', 'Air Quality Index': 3, 'Humidity': '70%'},
        'Vancouver':{'Temperature': '18*C', 'Air Quality Index': 2, 'Humidity': '60%'},
        'Toronto': {'Temperature': '16*C', 'Air Quality Index': 5, 'Humidity': '65%'}        
            }
    def __init__(self, city='', temperature='', aqi=0, humidity=''):
        self.city = city
        self.temperature = temperature
        self.aqi = aqi
        self.humidity = humidity

    @classmethod
    def view_city(cls, city):
        temperature = cls.weather_dict[city]['Temperature'] # when adding extra strings to a value, you have to access the value before.
        print(f"City: {city}")
        print(f"Temperature: {temperature}*C")  # value accessed, strings added.
        print(f"Air Quality Index: {cls.weather_dict[city]['Air Quality Index']}")
        print(f"Humidity: {cls.weather_dict[city]['Humidity']}")

    @classmethod
    def add_city(cls, city, temperature, aqi, humidity):
        cls.weather_dict[city] = {'Temperature': temperature, 'Air Quality Index': aqi, 'Humidity': humidity}

class WeatherApp: # Make a new class for the main applicaiton loop.
    def run(self): # Put the entire main appplication Loop in the function
        while True:
            welcome_input = get_valid_input("""Welcome to the Weather App! Please enter one of the following:
        1: View City
        2: Add City
        3: View All Cities
        4: Exit
            """, ['1', '2', '3', '4'], exit_avail = True)

            if welcome_input == '1':
                 self.view_city_input()
            elif welcome_input == '2':
                 self.add_city_input()
            elif welcome_input == '3':
                 self.view_all_cities()
            elif welcome_input == '4':
                 print('Goodbye!')
                 break

    def view_all_cities(self): # Added new functionality: View all cities.
         print(WeatherDatabase.weather_dict)


    def view_city_input(self): # turning each functionality into its own method within the class.
                while True:
                    city = input('What city would you like to view?')
                    city = city.title()
                    if city in WeatherDatabase.weather_dict:
                        WeatherDatabase.view_city(city)
                        break
                    else:
                        print('Error: city not found.')
                        break

    
    def add_city_input(self):
                
                while True:
                    city = input('Enter the city your would like to add:')
                    city = city.title()
                    if city in WeatherDatabase.weather_dict:
                        print('Error: City already in weather app.')
                        continue
                    else:
                        temperature = input(f'Enter the temperature for {city} in celsius (only enter numbers):')
                        aqi = int(input(f'Enter the Air Quality Index for {city}:'))
                        humidity = input(f'Enter the humidity for {city}:')
                        break
                app = WeatherDatabase(city, temperature, aqi, humidity)
                app.add_city(city, temperature, aqi, humidity)
                print(f'{city} Added Successfully!')
                print(WeatherDatabase.weather_dict[city])


def get_valid_input(prompt, valid_responses, exit_avail=True):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == '4' and exit_avail:
            print('Goodbye!')
            exit()
        elif user_input in valid_responses:
            return user_input # Returning user input back to the function call
        else:
            print("I didn't get that, please try again.")

app = WeatherApp()
app.run() # calling the method within the class
