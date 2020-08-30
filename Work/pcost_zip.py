import csv
import sys

def portfolio_cost(filename):
    total = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    list = []
    #    with open(filename, 'rt') as f: # read file line by line
    #        headers = (next(f))
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
                shares = int(record['shares'])
                price = float(record['price'])
                total = total + (shares * price)
        except ValueError:
            print("Input file is invalid")
    return total


if (len(sys.argv)) == 2:
    filename = sys.argv[1]  # read filename input from user
else:
    filename = 'Data/portfolio.csv' # default to this file if no input

total = portfolio_cost(filename)
print('Total cost: ', total)


