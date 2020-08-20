
total = 0
with open('Data/portfolio.csv', 'rt') as f: # read file line by line
    headers = (next(f))
    for line in f:
        stock = line.split(',')
        shares = int(stock[1])
        price = float(stock[2])
        total = total + (shares * price)
        print(line, end='')

print(total)


