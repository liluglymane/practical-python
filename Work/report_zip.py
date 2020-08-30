import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        record = dict(zip(headers, row))
        stock = {'name': record['name'], 'shares': int(record['shares']), 'price' : float(record['price'])}
        portfolio.append(stock)
    return portfolio

def read_prices(filename):
    f = open(filename)
    rows = csv.reader(f)
    prices={}   # create empty dictionary
    for row in rows:
        try:
            prices[row[0]] = row[1]  # read values from file and assign keys in dictionary
        except IndexError:
            print("Input file is invalid")

    return prices

if (len(sys.argv)) == 2:
    filename = sys.argv[1]  # read filename input from user
    filename2 = sys.argv[1]  # read filename input from user
else:
    filename = 'Data/portfolio.csv' # default to this file if no input
    filename2 = 'Data/prices.csv'  # default to this file if no input

portfolio_old = read_portfolio(filename)
portfolio_new = read_prices(filename2)

# pprint(portfolio_old)   # old stock price values
# pprint(portfolio_new)   # new stock price values

"""
total = 0
for name, shares, price in portfolio:   # portfolio list containing tuples is now like a 2D array and can be accessed with portfolio[row][column]
    total += shares * price
print(total)
"""

total = 0
total_new=0
for s in portfolio_old:   # portfolio list containing dictionary
    total += s['shares'] * s['price']
    total_new += float(portfolio_new[s['name']]) * s['shares'] # find and calculate stock price of shares using names from original portfolio as index for dictionary containing new prices

print('\nTotal value of old portfolio = ' + str(total))
print('Total value of new portfolio = ' + str(total_new))

