# Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

# Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

# In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number of Bitcoins, 
# , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
# import requests

# try:
#     ...
# except requests.RequestException:
#     ...
# Outputs the current cost of n
#  Bitcoins in USD to four decimal places, using , as a thousands separator.

import requests
import sys
import json
from config import API_key

try:
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_key}")
    data = response.json()
except requests.RequestException:
    sys.exit("Request failed")
    
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    bitcoin = float(sys.argv[1])
    price = float(data["data"]["priceUsd"])
    amount = bitcoin * price
    print(f"${amount:,.4f}")
except:
    sys.exit("Command-line argument is not a number") 
    

    
   