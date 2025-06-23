import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.dates as mdates
import time

cript = '''
        Здравствуй юный трейдер на криптие
    1 - BTC
    2 - ATOM
    3 - AVAX
    4 - DOGE
    5 - ETH
    6 - XLM
    7 - BNBN
    8 - DOT
    9 - LINK
    10 - LTC
    11 - APT
    0 - убежать от проблем и скриться от рынка
        И запомни выигрывают единцы
        УДАЧИ!
'''

def calculate_ema(prices, days):
    ema = prices.ewm(span=days, adjust=False).mean()
    return ema

def calculate_macd(prices):
    ema_12 = calculate_ema(prices, 12)
    ema_26 = calculate_ema(prices, 26)
    macd_line = ema_12 - ema_26
    signal_line = calculate_ema(macd_line, 9)
    macd_histogram = macd_line - signal_line
    return macd_line, signal_line, macd_histogram

def calculate_index_strength(prices, volumes):
    index_strength = (prices.diff() * volumes).dropna()
    return index_strength

def calculate_bull_bear_strength(prices, ema):
    bull_strength = prices.rolling(window=22).max() - ema
    bear_strength = prices.rolling(window=22).min() - ema
    return bull_strength, bear_strength

def calculate_stochastic_oscillator(prices, window):
    min_price = prices.rolling(window=window).min()
    max_price = prices.rolling(window=window).max()
    stochastic_oscillator = ((prices - min_price) / (max_price - min_price)) * 100
    return stochastic_oscillator

def vichislenia(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Не удалось получить данные с сервера. Проверьте URL и ваше интернет-соединение.")
        return

    data = response.json()

    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)

    # Добавляем столбец с объемами торгов
    df['volume'] = [item[1] for item in data['total_volumes']]

    average_price_22 = df['price'].rolling(window=22).mean()
    average_price_9 = df['price'].rolling(window=9).mean()

    ema_22 = calculate_ema(df['price'], 22)
    ema_9 = calculate_ema(df['price'], 9)

    macd_line, signal_line, macd_histogram = calculate_macd(df['price'])

    index_strength = calculate_index_strength(df['price'], df['volume'])

    bull_strength, bear_strength = calculate_bull_bear_strength(df['price'], ema_22)

    stochastic_oscillator_10 = calculate_stochastic_oscillator(df['price'], 10)
    stochastic_oscillator_20 = calculate_stochastic_oscillator(df['price'], 20)

    fig = plt.figure(figsize=(14, 10))
    gs = gridspec.GridSpec(2, 2, height_ratios=[3, 1], width_ratios=[1, 1])

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])

    # Первый график: цены и EMA
    ax1.plot(df.index, df['price'], label='Цена', color='blue')
    ax1.plot(df.index, ema_22, label='EMA 22', color='orange')
    ax1.plot(df.index, ema_9, label='EMA 9', color='green')
    ax1.set_title('Цены и EMA')
    ax1.set_xlabel('Дата')
    ax1.set_ylabel('Цена')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
    ax1.legend()

    # Второй график: объемы торгов
    ax2.plot(df.index, df['volume'], label='Объемы', color='red')
    ax2.set_title('Объемы торгов')
    ax2.set_xlabel('Дата')
    ax2.set_ylabel('Объем')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
    ax2.legend()

    # Сила быков и медведей
    ax3.bar(df.index, bull_strength, label='Сила быков', color='green')
    ax3.bar(df.index, bear_strength, label='Сила медведей', color='red')
    ax3.set_title('Сила быков и медведей')
    ax3.set_xlabel('Дата')
    ax3.set_ylabel('Сила')
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
    ax3.legend()

    #Macd SignalLine
    ax4.plot(df.index, macd_line, label='MACD', color='blue')
    ax4.plot(df.index, signal_line, label='Сигнальная линия', color='green')
    ax4.plot(df.index, macd_histogram, label='MACD гистограмма', color='purple')
    ax4.set_title("MACD")
    ax4.set_xlabel('Дата')
    ax4.set_ylabel('число')
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax4.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)
    ax4.legend()

    print("Средняя цена за 22 дня:")
    print(average_price_22)
    print("\nСредняя цена за 9 дней:")
    print(average_price_9)
    print("\nEMA за 22 дня:")
    print(ema_22)
    print("\nEMA за 9 дней:")
    print(ema_9)
    print("\nMACD Line:")
    print(macd_line)
    print("\nSignal Line:")
    print(signal_line)
    print("\nMACD Histogram:")
    print(macd_histogram)
    print("\nИндекс силы:")
    print(index_strength)
    print("\nСила быков:")
    print(bull_strength)
    print("\nСила медведей:")
    print(bear_strength)
    print("\nStochastic Oscillator 10:")
    print(stochastic_oscillator_10)
    print("\nStochastic Oscillator 20:")
    print(stochastic_oscillator_20)

    plt.tight_layout()
    plt.show()

def vichislenia_5(url):
    while True:
        response = requests.get(url)
        if response.status_code != 200:
            print("Не удалось получить данные с сервера. Проверьте URL и ваше интернет-соединение.")
            break

        data = response.json()

        df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)

        # Добавляем столбец с объемами торгов
        df['volume'] = [item[1] for item in data['total_volumes']]

        average_price_110 = df['price'].rolling(window=110).mean()
        average_price_45 = df['price'].rolling(window=45).mean()

        ema_110 = calculate_ema(df['price'], 110)
        ema_45 = calculate_ema(df['price'], 45)

        macd_line_5, signal_line_5, macd_histogram_5 = calculate_macd(df['price'])

        index_strength = calculate_index_strength(df['price'], df['volume'])

        bull_strength_5, bear_strength_5 = calculate_bull_bear_strength(df['price'], ema_110)

        fig1 = plt.figure(figsize=(14, 10))
        gs = gridspec.GridSpec(2, 2, height_ratios=[3, 1], width_ratios=[1, 1])

        ax1 = fig1.add_subplot(gs[0, 0])
        ax2 = fig1.add_subplot(gs[0, 1])
        ax3 = fig1.add_subplot(gs[1, 0])
        ax4 = fig1.add_subplot(gs[1, 1])

        # Первый график: цены и EMA
        ax1.plot(df.index, df['price'], label='Цена', color='blue')
        ax1.plot(df.index, ema_110, label='EMA 110', color='orange')
        ax1.plot(df.index, ema_45, label='EMA 45', color='green')
        ax1.set_title('Цены и EMA')
        ax1.set_xlabel('Дата')
        ax1.set_ylabel('Цена')
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
        ax1.legend()

        # Второй график: объемы торгов
        ax2.plot(df.index, df['volume'], label='Объемы', color='red')
        ax2.set_title('Объемы торгов')
        ax2.set_xlabel('Дата')
        ax2.set_ylabel('Объем')
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax2.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
        ax2.legend()

        # Сила быков и медведей
        ax3.bar(df.index, bull_strength_5, label='Сила быков', color='green')
        ax3.bar(df.index, bear_strength_5, label='Сила медведей', color='red')
        ax3.set_title('Сила быков и медведей')
        ax3.set_xlabel('Дата')
        ax3.set_ylabel('Сила')
        ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax3.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
        ax3.legend()

        # Macd SignalLine
        ax4.plot(df.index, macd_line_5, label='MACD', color='blue')
        ax4.plot(df.index, signal_line_5, label='Сигнальная линия', color='green')
        ax4.plot(df.index, macd_histogram_5, label='MACD гистограмма', color='purple')
        ax4.set_title("MACD")
        ax4.set_xlabel('Дата')
        ax4.set_ylabel('число')
        ax4.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax4.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)
        ax4.legend()

        plt.tight_layout()
        plt.show()



print(cript)
tr = input("Введите число:")
while tr != '0':
    if tr == '1':
        variant = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)
        break



    elif tr == '2':
        variant = "https://api.coingecko.com/api/v3/coins/cosmos/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '3':
        variant = "https://api.coingecko.com/api/v3/coins/avalanche-2/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '4':
        variant = "https://api.coingecko.com/api/v3/coins/dogecoin/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '5':
        variant = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '6':
        variant = "https://api.coingecko.com/api/v3/coins/stellar/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '7':
        variant = "https://api.coingecko.com/api/v3/coins/binancecoin/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '8':
        variant = "https://api.coingecko.com/api/v3/coins/polkadot/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '9':
        variant = "https://api.coingecko.com/api/v3/coins/chainlink/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '10':
        variant = "https://api.coingecko.com/api/v3/coins/litecoin/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '11':
        variant = "https://api.coingecko.com/api/v3/coins/aptos/market_chart?vs_currency=usd&days=365&interval=daily"
        vichislenia(variant)
        vichislenia_5(variant)

    elif tr == '0':
        break

    else:
        print("Ты чета попутал дядя")

    tr = input("Введите число:")

print("Удачи")