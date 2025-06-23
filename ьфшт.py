import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data(symbol, start_date, end_date, interval='daily'):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart?vs_currency=usd&from={start_date}&to={end_date}&interval={interval}"
    response = requests.get(url)
    data = response.json()
    prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
    prices.set_index('timestamp', inplace=True)
    return prices

def calculate_ema(prices, days):
    return prices.ewm(span=days, adjust=False).mean()

def calculate_macd(prices):
    ema_12 = calculate_ema(prices, 12)
    ema_26 = calculate_ema(prices, 26)
    macd_line = ema_12 - ema_26
    signal_line = calculate_ema(macd_line, 9)
    macd_histogram = macd_line - signal_line
    return macd_line, signal_line, macd_histogram

def calculate_stochastic_oscillator(prices, window):
    min_price = prices.rolling(window=window).min()
    max_price = prices.rolling(window=window).max()
    stochastic_oscillator = ((prices - min_price) / (max_price - min_price)) * 100
    return stochastic_oscillator

# Get data for Bitcoin
bitcoin_prices = fetch_data('bitcoin', 1643723400000, 1712211199, 'daily')

# Calculate indicators
ema_12 = calculate_ema(bitcoin_prices['price'], 12)
ema_26 = calculate_ema(bitcoin_prices['price'], 26)
macd_line, signal_line, macd_histogram = calculate_macd(bitcoin_prices['price'])
stochastic_oscillator_10 = calculate_stochastic_oscillator(bitcoin_prices['price'], 10)
stochastic_oscillator_20 = calculate_stochastic_oscillator(bitcoin_prices['price'], 20)

# Plotting
plt.figure(figsize=(14, 10))

plt.subplot(4, 1, 1)
plt.plot(bitcoin_prices.index, bitcoin_prices['price'], label='Price')
plt.plot(ema_12.index, ema_12, label='EMA 12')
plt.plot(ema_26.index, ema_26, label='EMA 26')
plt.title('Bitcoin Price and EMA')
plt.legend()

plt.subplot(4, 2, 3)
plt.plot(macd_line.index, macd_line, label='MACD Line')
plt.plot(signal_line.index, signal_line, label='Signal Line')
plt.bar(macd_histogram.index, macd_histogram, label='MACD Histogram')
plt.title('MACD')
plt.legend()

plt.subplot(4, 2, 4)
plt.plot(stochastic_oscillator_10.index, stochastic_oscillator_10, label='Stochastic Oscillator 10')
plt.plot(stochastic_oscillator_20.index, stochastic_oscillator_20, label='Stochastic Oscillator 20')
plt.title('Stochastic Oscillator')
plt.legend()

plt.tight_layout()
plt.show()