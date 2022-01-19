# with open("weather_data.csv", mode = "r") as data_file:
#     data = (data_file.readlines())

#========================================================

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

#========================================================

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data)

# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# print(data["temp"].max())

# print(data.day)

# print(data[data.temp == data.temp.max()])

#==================================================

# monday = data[data.day == "Monday"]

# def cel_to_fahr(temp_cel):
#     temp_fahr = temp_cel * (9/5) + 32
#     print(temp_fahr)

# cel_to_fahr(int(monday.temp))

#==================================================

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#==================================================

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

print(data_dict)

data_final = pandas.DataFrame(data_dict)
data_final.to_csv("squirrel_data.csv")