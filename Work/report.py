import csv
import sys
from pprint import pprint

def portfolio_cost(filename):
    total = 0
    f = open(filename)
    rows = csv.reader(f)
    next(rows)
    #    with open(filename, 'rt') as f: # read file line by line
    #        headers = (next(f))
    for row in rows:
        try:
                shares = int(row[1])
                price = float(row[2])
                total = total + (shares * price)
        except ValueError:
            print("Input file is invalid")
    return total


def read_portfolio(filename):
    portfolio = []
    f = open(filename)
    rows = csv.reader(f)
    next(rows)

    """""
    for row in rows:
        try:
            holding = (row[0], int(row[1]), float(row[2]))  # read create tuples of values from file
            portfolio.append(holding)   # append list with tuples
        except ValueError:
            print("Input file is invalid")
    """

    for row in rows:
        try:
            holding = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}  # read create tuples of values from file
            portfolio.append(holding)   # append list with tuples
        except ValueError:
            print("Input file is invalid")

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

def print_report(portfolio_old, portfolio_new):
    total = 0
    total_new = 0
    for s in portfolio_old:  # portfolio list containing dictionary
        total += s['shares'] * s['price']
        total_new += float(portfolio_new[s['name']]) * s['shares']  # find and calculate stock price of shares using names from original portfolio as index for dictionary containing new prices

    print('\nTotal value of old portfolio = ' + str(total))
    print('Total value of new portfolio = ' + str(total_new))


if (len(sys.argv)) == 2:
    filename = sys.argv[1]  # read filename input from user
    filename2 = sys.argv[1]  # read filename input from user
else:
    filename = 'Data/portfolio.csv' # default to this file if no input
    filename2 = 'Data/prices.csv'  # default to this file if no input

portfolio_old = read_portfolio(filename)
portfolio_new = read_prices(filename2)
print_report(portfolio_old, portfolio_new)


"""
total = 0
for name, shares, price in portfolio:   # portfolio list containing tuples is now like a 2D array and can be accessed with portfolio[row][column]
    total += shares * price
print(total)
"""


