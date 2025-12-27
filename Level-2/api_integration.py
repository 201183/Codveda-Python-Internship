import requests
def fetch_weather(city):
    try:
        # Free API: wttr.in, JSON format
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error if HTTP response is bad
        data = response.json()

        # Parse weather information
        current_condition = data['current_condition'][0]
        temp_c = current_condition['temp_C']
        temp_f = current_condition['temp_F']
        weather_desc = current_condition['weatherDesc'][0]['value']
        humidity = current_condition['humidity']

        # Display weather info
        print(f"\n--- Weather in {city.capitalize()} ---")
        print(f"Temperature: {temp_c}°C / {temp_f}°F")
        print(f"Condition: {weather_desc}")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API!")
    except requests.exceptions.Timeout:
        print("Error: Request timed out!")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except (KeyError, IndexError, TypeError):
        print("Error: Unexpected data format received from API!")
# Menu-driven program
while True:
    print("\n--- Task 3: Weather Information ---")
    print("1. Get Weather")
    print("2. Exit")
    choice = input("Select an option: ")
    if choice == "1":
        city = input("Enter city name: ").strip()
        if city:
            fetch_weather(city)
        else:
            print("City name cannot be empty.")
    elif choice == "2":
        print("Exiting program.")
        break
    else:
        print("Invalid option! Please choose 1 or 2.")

    
