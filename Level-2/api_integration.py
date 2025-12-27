import requests

def fetch_api_data():
    # Example: Fetch cryptocurrency prices from CoinGecko API
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises an error for bad status codes
        data = response.json()

        # Display data
        print("\n--- Cryptocurrency Prices (USD) ---")
        for coin, info in data.items():
            print(f"{coin.capitalize()}: ${info['usd']}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API!")
    except requests.exceptions.Timeout:
        print("Error: The request timed out!")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except KeyError:
        print("Error: Unexpected data format received from API!")

# Main program
while True:
    print("\n1. Fetch Cryptocurrency Prices")
    print("2. Exit")
    
    try:
        choice = int(input("Select an option: "))
        if choice == 1:
            fetch_api_data()
        elif choice == 2:
            print("Exiting API Integration Program.")
            break
        else:
            print("Invalid option. Choose 1 or 2.")
    except ValueError:
        print("Please enter a valid number.")
    