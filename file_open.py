total_price = 0
# with open("cafe-data.csv","r") as f:
#         content=f.read()
#         # header=next(f)
#         for line in content:
#             line = line.strip()
#             columns = line.split(',')
#             columns[0] = columns[0].strip('"')
#             columns[1] = float(columns[1])
#             columns[2] = float(columns[2])
#             columns[3] = int(columns[3])
#             columns[4] = columns[4].strip('"')
#             total_price += columns[2] * columns[3]
# print("Total price =", total_price)
#
import csv
import collections
from collections import OrderedDict
# f=open("cafe-data.csv","r")
# rows = csv.reader(f)
# header=next(rows)
# for row in rows:
#     print(row[3])
# for line in rows:
#     line = line.strip()
#     columns = line.split(',')
#     columns[0] = columns[0].strip('"')
#     columns[1] = float(columns[1])
#     columns[2] = float(columns[2])
#     columns[3] = int(columns[3])
#     columns[4] = columns[4].strip('"')
#     total_price += columns[2] * columns[3]
# print("Total price =", total_price)
total_price=0
# for row in rows:
#     row[3] = float(row[3])
#     row[4] = int(row[4])
#     total_price += row[3] * row[4]
# print("Total price = %10.2f " % total_price)

# f2=list(csv.DictReader(open("cafe-data.csv")))
# print((f2))

# dd=OrderedDict(([('date', '2016-06-12'), ('metal', 'Gold'), ('radius', '5.5'),('price', '80.99'), ('quantity', '1')]))
# print(dd)
with open('cafe-data.csv','r') as f3:
    r = csv.reader(f3)
    od = collections.OrderedDict((row[0], row[1:]) for row in r)
print(od)


# for item in od:
#     print(item['2016'])
# # fff=([row['date'] for row in od])