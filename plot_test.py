import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # For non-interactive plotting


# Data
timestamps = ['2021-01-01 09:30:00', '2021-01-01 09:35:00', '2021-01-01 09:40:00', '2021-01-01 09:45:00', '2021-01-01 09:50:00']

closing_prices = [100, 105, 110, 115, 120]

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(timestamps, closing_prices, marker='o')
plt.xlabel('Timestamp')
plt.ylabel('Closing Price')
plt.title('Stock Prices')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()