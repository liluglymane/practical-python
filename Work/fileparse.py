import csv

# select=None allows user option to select specific columns
# types=None allows to convert data types
# has_headers=None specifies if file being parsed has headers
# delimiter=None allows files to be parsed which have columns seperated in a different manner (comman, space etc)
def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=None):
    '''
    Parse a CSV file into a list of records
    '''

    if select and not has_headers: # raise exception if select and has_headers=False is passed as both cannot be selected
        raise RuntimeError('select requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)  # read file headers
        headers = next(rows) if has_headers else [] # headers = column headings unless has_headers=false

        records = []
        indices = []

        # if a column selector was given, find indices of the specified columns
        if select:
            indices = [headers.index(colname) for colname in select]  # map selected column names to column indices
            headers = select  # assign headers value to selected columns

        for row in rows:
            # skip rows with no data
            if not row:
                continue

            # align the selected columns with the correct value
            if select:
                row = [row[index] for index in indices]

            # convert values to the types given when function is called
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e: # if value could not be converted throws exception and prints it and continues code
                    if not silence_errors: # if silence_errors=true then skip errors and continue
                        print(f"Row {row}: Couldn't convert {row}")
                        print(f"Row {row}: Reason {e}")
                    continue

            # if headers are true then make dictionary otherwise make list of tuples instead
            if headers:
                record = dict(zip(headers, row)) # make a dictionary
            else:
                record = tuple(row) # if no headers in file than produce list of tuples instead as there are no column names

            records.append(record)

    return records

portfolio = parse_csv('Data/portfolio.csv', select=['name','price']) # select which columns to show
print(portfolio)

portfolio2 = parse_csv('Data/portfolio.csv', types=[str, int, float]) # select what column type is
print(portfolio2)

portfolio3 = parse_csv('Data/portfolio.csv') # show all columns in file with no type conversion
print(portfolio3)

portfolio4 = parse_csv('Data/prices.csv', has_headers=False) # parse file with no headers
print(portfolio4)

portfolio5 = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ') # parse a file with space as the delimiter
print(portfolio5)

# portfolio6 = parse_csv('Data/missing.csv', types=[str, int, float]) # will throw a Runtime error as cannot have columns selected and has_headers=false
# print(portfolio6)

# portfolio6 = parse_csv('Data/missing.csv', types=[str, int, float])# will throw an exception as not all values could be converted
# print(portfolio6)

portfolio6 = parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True) # silence all exceptions/errors
print(portfolio6)