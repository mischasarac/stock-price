from datetime import datetime
import json

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")

with open("sampleCoin.json", 'r') as f:
  data = json.load(f)
  print(formatted_date)
  print(((data['status'])['timestamp'])[0:10])
  if ((data['status'])['timestamp'])[0:10] == formatted_date:
    print("Data is up to date")

print(f"Current date and time: {formatted_date}")