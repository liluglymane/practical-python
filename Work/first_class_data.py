import csv
import sys
from pprint import pprint

types = [str, int, float]

f = open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

print(row[1])
print(types[1](row[1])) # same as int(row[1])
print(types[2](row[2])) # same as float(row[2])
print(types[1](row[1])*types[2](row[2]))

r = list(zip(types, row))
print(r)

converted = []
for func, val in zip(types, row): # zipped list allows for conversion of all values
    converted.append(func(val)) # func is variable of one of the type conversions (str, int, float) and val is variable (AA, 100)

print(converted)

converted = [func(val) for func, val in zip(types, row)] # compressed version of above code



def date_to_tuple(datestring):
   return tuple(int(part) for part in datestring.split('/')) # converts 6/11/2007 from excel to tuple

f = open('Data/dowstocks.csv') # convert fields from any excel to object
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
types = [str, float, date_to_tuple, str, float, float, float, float, int] # match data type of headers
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
print(record)

