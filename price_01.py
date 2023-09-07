import csv
import glob


def ring_cost(filename):
    ''' calculate the total cost '''
    total_price = 0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            row[3] = float(row[3])  # price
            row[4] = int(row[4])  # quantity
            print(row[3],row[4])
            total_price += row[3] * row[4]
    print(total_price)
    return total_price
(glob.glob('*.csv'))
files = glob.glob('*.csv')
files2 = glob.glob('*.csv')
files.extend(files2) # extend list
print(files)
def main():
    total = ring_cost('cafe-data.csv') # function call
    # print("Total price = %10.2f " % total) #
if __name__ == '__main__':
    main()
