import csv
import sys

def portfolio_cost(filename):
    total = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
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

if (len(sys.argv)) == 2:
    filename = sys.argv[1]  # read filename input from user
else:
    filename = 'Data/portfolio.csv' # default to this file if no input

total = portfolio_cost(filename)
print('Total cost: ', total)


