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
else:
    filename = 'Data/prices.csv' # default to this file if no input

portfolio = read_prices(filename)
pprint(portfolio)


