import sys
import os
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # Define bitcoin value from argument
        bitcoin_value = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # Define bitcoin value from argument
        bitcoin_value = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:

        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c48ccd044b66dd320cf9fd684bd906993a77d8d7b828e04319688454ace86612")

        # Extract and parse the price
        bitcoin_price = float(response.json()['data']['priceUsd'])

        # Calculate and display result
        result = bitcoin_value * bitcoin_price
        print(f"${result:,.4f}")

    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price.")
    except KeyError:
        sys.exit("Unexpected response format from API.")

        # Extract and parse the price
        bitcoin_price = float(response.json()['data']['priceUsd'])

        # Calculate and display result
        result = bitcoin_value * bitcoin_price
        print(f"${result:,.4f}")

    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price.")
    except KeyError:
        sys.exit("Unexpected response format from API.")


if __name__ == "__main__":
    main()
