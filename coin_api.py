from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from datetime import datetime

# API request perameters

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

# Check if the data is up to date
# If the data is not up to date, load the data

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
dateLen = len(formatted_date)

# Check if the data exists
if os.path.exists('sampleCoin.json'):
  with open('sampleCoin.json', 'r') as f:

    data = json.load(f)
    if((data['status'])['timestamp'][0:dateLen] == formatted_date): # Check if date on JSON file matches with today's date
      print("Data loaded successfully")
    else:
      print("Data is not up to date")
      print("Updating data")
      
      try: # Making API request
        response = session.get(url, params=parameters) 
        data = json.loads(response.text)
        
        with open('sampleCoin.json', 'w') as f:
          json.dump(data, f)
          
        print(data)
        
      except (ConnectionError, Timeout, TooManyRedirects) as e: # Error handling
        print(e)
# If the data does not exist, load the data from API
else:
    
    print("Data does not exist")
    print("Loading data")
    
    try: # Making API request
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        
        with open('sampleCoin.json', 'w') as f:
          json.dump(data, f)
          
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e: # Error handling
        print(e)
        

          
