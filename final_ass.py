import yfinance as yf

# Create a ticker object for Tesla (TSLA)
tesla_ticker = yf.Ticker("TSLA")

# Extract stock information and save it in a dataframe named tesla_data
tesla_data = tesla_ticker.history(period='max')

# Print the first few rows of the dataframe
print(tesla_data.head())


import requests
from bs4 import BeautifulSoup
url = "https://finance.yahoo.com/quote/TSLA/financials?p=TSLA"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print(tesla_data.tail(5))
gamestop_ticker = yf.Ticker("GME")


# Extract stock information and save it in a dataframe named gamestop_data
gamestop_data = gamestop_ticker.history(period='max')

# Print the first few rows of the dataframe
print(gamestop_data.head())

import requests
from bs4 import BeautifulSoup
url = "https://finance.yahoo.com/quote/GME/financials?p=GME"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
revenue_element = soup.find("span", class_="Trsdu(0.3s)")
revenue = revenue_element
print("GameStop's revenue:", revenue)

import matplotlib.pyplot as plt

# Create a ticker object for GameStop (GME)
gamestop_ticker = yf.Ticker("GME")

# Extract stock information for a specific period (e.g., 1 year)
gamestop_data = gamestop_ticker.history(period='1y')

pip install Flask

# Plot the stock prices
plt.figure(figsize=(10, 6))
plt.plot(gamestop_data['Close'], label='Closing Price', color='blue')
plt.title('GameStop (GME) Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
