# with open("weather.csv") as data_file:
#     data=data_file.readlines()
#     print(data)
# import csv
# with open("weather.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#         print(row)
#     print(temperatures)


import pandas
# data=pandas.read_csv("weather.csv")
# print(data)
# data_dict=data.to_dict()
# print(data_dict)
# temp_list=data["temp"].to_list()
# print(len(temp_list))
#
# print(sum(temp_list)/len(temp_list))
# data["temp"].mean()
# maximum=data["temp"].max()
# print(maximum)
# print(data["condition"])
# print(data.condition)
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# student_dict={
#     "students":["mori","david","john"],
#     "scores":[70,90,60]
# }
# data=pandas.DataFrame(student_dict)
# (data.to_csv("new_data.csv"))
# my_data=pandas.read_csv("new_data.csv")
# print(my_data)
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])
data_dict={
    "color":["Gray","Cinnamon","Black"],
    "count":[gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}
df=pandas.DataFrame(data_dict)
df.to_csv("squirrels_count")