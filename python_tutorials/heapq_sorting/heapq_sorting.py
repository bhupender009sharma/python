import heapq

grades = [132,54,76,7,8,74343,45,657]
print(heapq.nlargest( 3 , grades) )

stocks = [
    {'ticker': 'GOOG','price': 1419.85},
    {'ticker': 'AAPL','price': 342.99},
    {'ticker':'AMZN','price': 2572.68},
    {'ticker':'MSFT','price': 188.94},
    {'ticker':'EBAY','price': 47.89}
]

print(heapq.nsmallest(2,stocks, key=lambda stock: stock['price']))