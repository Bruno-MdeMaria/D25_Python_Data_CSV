# import csv
# with open("weather_data.csv") as data_value:
#     data = csv.reader(data_value)
#     temperaturas = []
#     for linha in data:
#        if linha[1] != "temp":  #necessário esta condição apra não puxar a palavra "temp" que está na coluna températuras e puxar somente os valores.
#         temperaturas.append(int(linha[1]))
#     print(temperaturas)

#COM A BLIBLIOTECA PANDAS:

import pandas
data = pandas.read_csv("weather_data.csv")

data_dicio = data.to_dict()  #tranforma um DATAFRAME(planilha) em um dicionario.
data_list = data["temp"].to_list #transforma uma SERIES(coluna) em lista.


           
