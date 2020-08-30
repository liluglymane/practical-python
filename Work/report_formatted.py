import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    portfolio = []  # create empty list
    f = open(filename)
    rows = csv.reader(f)
    next(rows)

    for row in rows:
        try:
            holding = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}  # read create tuples of values from file
            portfolio.append(holding)   # append list with tuples
        except ValueError:
            pass

    return portfolio

def read_prices(filename):
    prices = {}   # create empty dictionary
    f = open(filename)
    rows = csv.reader(f)

    for row in rows:
        try:
            prices[row[0]] = row[1]  # read values from file and assign keys in dictionary
        except IndexError:
            pass

    return prices

def make_report(portfolio_old,portfolio_new):
    rows = []
    for s in portfolio_old:  # portfolio list containing dictionary
        current_price = float(portfolio_new[s['name']])    # get current price from dictionary
        change = current_price - float(s['price'])   # find out change of price
        summary = (s['name'], s['shares'], current_price, change)   # creating tuple of name, shares, price and change
        rows.append(summary) # add tuple to list
    return rows


if (len(sys.argv)) == 2:
    filename = sys.argv[1]  # read filename input from user
    filename2 = sys.argv[1]  # read filename input from user
else:
    filename = 'Data/portfolio.csv' # default to this file if no input
    filename2 = 'Data/prices.csv'  # default to this file if no input

portfolio_old = read_portfolio(filename)
portfolio_new = read_prices(filename2)

report = make_report(portfolio_old, portfolio_new)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)  # addings headers
print(('-' * 10 + ' ') * len(headers))  # add underline to headers
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)    # format output of list
# pprint(portfolio_old)   # old stock price values
# pprint(portfolio_new)   # new stock price values

"""
total = 0
for name, shares, price in portfolio:   # portfolio list containing tuples is now like a 2D array and can be accessed with portfolio[row][column]
    total += shares * price
print(total)
"""

