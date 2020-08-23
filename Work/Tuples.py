import csv

f = open('C:/Users/Ibrahim/practical-python/Work/Data/portfolio.csv')
rows = csv.reader(f)
next(rows)
for row in rows:
    t = (row[0], int(row[1]), float(row[2])) # assigning variables to tuple
    print (t[0])
    print (t[1] * t[2])
    name, shares, price = t # unpacking a tuple to individual variables
    print(name, shares, price)