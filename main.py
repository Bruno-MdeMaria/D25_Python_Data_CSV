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
temp_list = data["temp"].to_list() #transforma uma SERIES(coluna) em lista.
print(temp_list)

#VERIFICAR TEMPERATURA MÉDIA:
# soma = 0
# for temp in temp_list:
#     soma += temp
# media = soma / len(temp_list)
# print(media)

#NO PANDAS:
print(data["temp"].mean())

#MAIOR TEMPERATURA:
print(data["temp"].max())   #forma de chamar uma coluna e enontrar o valor máximo da mesma.
print(data.temp.max())   #forma de chamar uma coluna... tratado ela como um atributo de um objeto.

#LINHA ONDE A MAIOR TEMPERATUDA SE ENCONTRA:
max = data.temp.max()         
print(data[data.temp == max])
#outra forma:
print(data[data.temp == data.temp.max()])



           
