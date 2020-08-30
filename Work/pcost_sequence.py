import csv
import sys

def portfolio_cost(filename):
    total = 0
    f = open(filename)
    rows = csv.reader(f)
    next(rows)
    #    with open(filename, 'rt') as f: # read file line by line
    #        headers = (next(f))
    for rowno, row in enumerate(rows, start=1):
        try:
                shares = int(row[1])
                price = float(row[2])
                total = total + (shares * price)
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    return total

if (len(sys.argv)) == 2:
    filename = sys.argv[1]  # read filename input from user
else:
    filename = 'Data/missing.csv' # default to this file if no input

total = portfolio_cost(filename)
print('Total cost: ', total)


