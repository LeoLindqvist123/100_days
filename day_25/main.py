'''import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

'''

#import pandas

#data = pandas.read_csv("weather_data.csv")

#temp_list = data["temp"].to_list()
#print(len(temp_list))

#print(data["temp"].max())

#print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#monday_temp = monday.temp[0]
#monday_temp_f = monday_temp * 9/5 + 32
#print(monday_temp_f)

import pandas

data = pandas.read_csv("squirrels.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)