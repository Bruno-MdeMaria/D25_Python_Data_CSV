import csv
with open("weather_data.csv") as data_value:
    data = csv.reader(data_value)
    for linha in data:
        print(linha)