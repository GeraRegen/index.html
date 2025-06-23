import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go


# Функция для получения данных
def fetch_data(ticker, period='1y', interval='1d'):
    data = yf.download(ticker, period=period, interval=interval)
    return data


# Функция для расчета индикаторов вручную
def calculate_indicators(data):
    # EMA
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()

    # MACD
    ema_12 = data['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = ema_12 - ema_26
    data['MACD_signal'] = data['MACD'].ewm(span=9, adjust=False).mean()
    data['MACD_hist'] = data['MACD'] - data['MACD_signal']

    # Stochastic Oscillators
    data['STOCH_K'] = ((data['Close'] - data['Low'].rolling(14).min()) / (
                data['High'].rolling(14).max() - data['Low'].rolling(14).min())) * 100
    data['STOCH_D'] = data['STOCH_K'].rolling(3).mean()

    return data


# Функция для визуализации данных
def plot_data(data, ticker, interval):
    fig = go.Figure()

    # Свечной график
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'],
                                 name='Свечной график'))

    # EMA
    fig.add_trace(go.Scatter(x=data.index, y=data['EMA_20'], name='EMA 20'))

    # MACD
    fig.add_trace(go.Scatter(x=data.index, y=data['MACD'], name='MACD'))
    fig.add_trace(go.Scatter(x=data.index, y=data['MACD_signal'], name='Signal Line'))
    fig.add_trace(go.Bar(x=data.index, y=data['MACD_hist'], name='MACD Histogram'))

    # Stochastic Oscillators
    fig.add_trace(go.Scatter(x=data.index, y=data['STOCH_K'], name='%K'))
    fig.add_trace(go.Scatter(x=data.index, y=data['STOCH_D'], name='%D'))

    fig.update_layout(title=f'{ticker} ({interval}) - Технические индикаторы',
                      xaxis_title='Дата',
                      yaxis_title='Цена',
                      legend_title='Индикаторы')
    fig.show()


# Список криптовалют для анализа
tickers = ['BTC-USD', 'LTC-USD', 'LINK-USD', 'AVAX-USD', 'ATOM-USD', 'DOGE-USD', 'ETH-USD', 'BNB-USD']


# Основная функция
def main():
    for ticker in tickers:
        data = fetch_data(ticker)
        data = calculate_indicators(data)
        plot_data(data, ticker, '1d')


if __name__ == "__main__":
    main()
