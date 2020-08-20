with open('Data/portfolio.csv', 'rt') as f: # read file as one
    data = f.read()

print(data)


with open('Data/portfolio.csv', 'rt') as f: # read file line by line
    for line in f:
        print(line, end='')

