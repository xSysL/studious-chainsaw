import pandas
import csv

# data = pandas.read_csv("Working with CSV\\227 - weather-data.csv")


# temp_list = data["temp"].to_list()

# print(temp_list)

# print(data[data.temp == 12])

# print(data[data.temp == data["temp"].max()])

# def celcius_to_farhenheit(celcius):
#     return (celcius*1.8) + 32


# monday = data[data.day == "Monday"]
# print(celcius_to_farhenheit(monday.temp))

data = pandas.read_csv(
    'Working with CSV\\229 - 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel CSV")
