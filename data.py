import yfinance as yf


def get_data():
    tickerSymbol = 'RELIANCE.NS'

    tickerData = yf.Ticker(tickerSymbol)

    return tickerData.history(period='1d', start='2023-01-01', end='2023-03-31')
