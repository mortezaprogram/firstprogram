import csv

filename = "price.csv"


def read_file(filename, mode='warn'):
    ''' read csv file and save data in the list '''
    # check for correct mode
    if mode not in ['warn', 'silent', 'stop']:
        raise ValueError("possible modes are 'warn', 'silent', 'stop'")
    ring_data = []  # create empty list to save data
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        header = next(rows)  # skip the header
        # change the types of the columns
        for row in rows:

            try:
                row[2] = float(row[2])  # radius
                row[3] = float(row[3])  # price
                row[4] = int(row[4])  # quantity
            except ValueError as err:  # process value error only
                if mode == 'warn':
                    print("Invalid data, row is skipped")
                    print('Row: {}, Reason : {}'.format(row_num, err))
                elif mode == 'silent':
                    pass  # do nothing
                elif mode == 'stop':
                    raise  # raise the exception
                continue
            # append data in list in the form of tuple
            row_dict = {'date': row[0],'metal' : row[1],'radius' : row[2],'price' : row[3],'quantity' : row[4]}
            ring_data.append(row_dict)
        return ring_data


def main():
    ring_data = read_file('price.csv')

    # total rows in the file
    ring_gold=[ring for ring in ring_data if ring["metal"]=="Gold"]
    for ring in ring_gold:
        print(ring)
        print("metal:{0}: radios:{1}".format(ring['metal'], ring['radius']))


if __name__ == '__main__':
    main()