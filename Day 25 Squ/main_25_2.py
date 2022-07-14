import pandas


# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# # print(data_dict)
#
# data_list = data["temp"].to_list()
# # print(data_list)
#
# # print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data["temp"].max()])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data["Primary Fur Color"])
# data["Primary Fur Color"].value_counts()
nowe_dane = data["Primary Fur Color"].value_counts()
nowe_dane.to_csv("wiewiorkilista.csv")
