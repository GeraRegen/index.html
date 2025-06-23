from flask import Flask, render_template
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go

app = Flask(__name__)

# Список криптовалют для анализа
tickers = ['BTC-USD', 'LTC-USD', 'LINK-USD', 'AVAX-USD', 'ATOM-USD', 'DOGE-USD', 'ETH-USD', 'BNB-USD']


# Функция для получения данных
def fetch_data(ticker, period='1y', interval='1d'):
    data = yf.download(ticker, period=period, interval=interval)
    return data


# Функция для расчета индикаторов
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


# Функция для создания графика
def create_plot(data, ticker, interval):
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

    fig.add_trace(go.Scatter(x=data.index, y=data['MACD'], name='MACD'))
    fig.add_trace(go.Scatter(x=data.index, y=data['MACD_signal'], name='Signal Line'))
    fig.add_trace(go.Bar(x=data.index, y=data['MACD_hist'], name='MACD Histogram'))

    # Stochastic Oscillators
    fig.add_trace(go.Scatter(x=data.index, y=data['STOCH_K'], name='%K'))
    fig.add_trace(go.Scatter(x=data.index, y=data['STOCH_D'], name='%D'))

    fig.update_layout(title=f'{ticker} ({interval}) - Технические индикаторы',
                      xaxis_title='Дата',
                      yaxis_title='Цена',
                      legend_title='Индикаторы',
                      template='plotly_dark')

    return fig.to_html()


@app.route('/')
def index():
    return render_template('layout.html', tickers=tickers)


@app.route('/daily/<ticker>')
def daily(ticker):
    data = fetch_data(ticker, interval='1d')
    data = calculate_indicators(data)
    plot = create_plot(data, ticker, '1d')
    return render_template('daily.html', ticker=ticker, plot=plot)


@app.route('/weekly/<ticker>')
def weekly(ticker):
    data = fetch_data(ticker, interval='1wk')
    data = calculate_indicators(data)
    plot = create_plot(data, ticker, '1wk')
    return render_template('weekly.html', ticker=ticker, plot=plot)


@app.route('/hourly/<ticker>')
def hourly(ticker):
    data = fetch_data(ticker, interval='1h')
    data = calculate_indicators(data)
    plot = create_plot(data, ticker, '1h')
    return render_template('hourly.html', ticker=ticker, plot=plot)


@app.route('/four_hours/<ticker>')
def four_hours(ticker):
    data = fetch_data(ticker, interval='4h')
    data = calculate_indicators(data)
    plot = create_plot(data, ticker, '4h')
    return render_template('four_hours.html', ticker=ticker, plot=plot)


if __name__ == "__main__":
    app.run(debug=True)