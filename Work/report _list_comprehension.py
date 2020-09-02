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

cost = sum(s['shares'] * s['price'] for s in portfolio_old)  # list comprehension to calculate total portfolio cost in single line
print(cost)

value = sum(s['shares'] * float(portfolio_new[s['name']]) for s in portfolio_old)  # list comprehension to calculate current value of portfolio
print(value)

more100 = [s for s in portfolio_old if s['shares'] > 100]   # print stocks with more than 100 shares
print(more100)

msftibm = [s for s in portfolio_old if s['name'] in {'MSFT','IBM'}]  # print stocks with names matching IBM MSFT
print(msftibm)

cost10k = [s for s in portfolio_old if s['shares'] * s['price'] > 1000]  # print stocks with total holdings over 1000
print(cost10k)

name_shares = [(s['name'], s['shares']) for s in portfolio_old]  # build list of tuples with list comprehension
print(name_shares)

unique_names = {s['name'] for s in portfolio_old}  # use curly brackets which provides unique values
print(unique_names)

holdings = {unique_names:0 for unique_names in unique_names}  # create list of dictionary pairs
print(holdings)

for s in portfolio_old:  # dictionary comprehension
    holdings[s['name']] += s['shares']
print(holdings)

portfolio_prices = {unique_names:portfolio_new[unique_names] for unique_names in unique_names}  # assign new portfolo prices to names of stock existing in unique_names dictionary
print(portfolio_prices)

"""
total = 0
total_new=0
for s in portfolio_old:   # portfolio list containing dictionary
    total += s['shares'] * s['price']
    total_new += float(portfolio_new[s['name']]) * s['shares'] # find and calculate stock price of shares using names from original portfolio as index for dictionary containing new prices

print('\nTotal value of old portfolio = ' + str(total))
print('Total value of new portfolio = ' + str(total_new))
"""
