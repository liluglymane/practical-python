import csv

f = open('Data/portfoliodate.csv')
rows = csv.reader(f)
headers = next(rows)

select = {'name', 'shares', 'price'} # list of columns that we require
indices = [headers.index(colname) for colname in select] # locating indices of above colums in csv file

row = next(rows)
record = {colname:row[index] for colname, index in zip(select, indices)} # read a row of data and turn it into dictionary using dictionary comprehension
print(record)

portfolio = [{colname: row[index] for colname, index in zip(select, indices)} for row in rows] # read entire file
print(portfolio)