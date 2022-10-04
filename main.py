import csv
with open("weather_data.csv") as data_value:
    data = csv.reader(data_value)
    temperaturas = []
    for linha in data:
       if linha[1] != "temp":  #necessário esta condição apra não puxar a palavra "temp" que está na coluna températuras e puxar somente os valores.
        temperaturas.append(linha[1])
    print(temperaturas)
           
