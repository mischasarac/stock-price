#%%

import requests
import json

#%%

import pandas as pd
import matplotlib.pyplot as plt



url = 'https://www.alphavantage.co/query?function=BRENT&interval=monthly&apikey=09LJ2A7QECTEVF7S'
r = requests.get(url)
print(r.json())
data = r.json()['data']

# print(data)

# Extract the time series data
# print(data)
print(type(data))

timestamps = []
for i in range(len(data)):
    timestamps.append(i)
    
reversed_timestamps = timestamps[::-1]
    
value = []
for i in data:
    value.append(float(i['value']))

print(value)

# Plot the data
plt.figure(figsize=(10, 5))
print("made it here")
plt.plot(reversed_timestamps, value, marker='o')
plt.xlabel('Timestamp')
plt.ylabel('Closing Price')
plt.title('Stock Prices')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('stock_prices.png')
plt.show()
# %%
