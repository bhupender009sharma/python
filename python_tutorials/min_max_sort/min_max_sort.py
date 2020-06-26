stocks = {
    'GOOG': 1419.85,
    'AAPL': 342.99,
    'AMZN': 2572.68,
    'MSFT': 188.94,
    'EBAY': 47.89
}
print(min(zip(stocks.values(),stocks.keys() ) ) )
print(max(zip(stocks.values(),stocks.keys() ) ) )
print(sorted(zip(stocks.values(),stocks.keys() ) ) )