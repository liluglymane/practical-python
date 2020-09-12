import csv


def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f: # allows user option to select specific columns
        rows = csv.reader(f)
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []

        for row in rows:
            if not row: # skip rows with no data
                continue
            if indices:
                row = [row[index] for index in indices]


            record = dict(zip(headers, row)) # make a dictionary
            records.append(record)

    return records

portfolio = parse_csv('Data/portfolio.csv', select=['name','shares'])
print(portfolio)