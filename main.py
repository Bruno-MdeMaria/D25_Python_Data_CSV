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

#TRANFORMAR TODA A LINHA EM VARIAVEL:
monday = data[data.day == "Monday"]
print(monday.condition)

#TRANFORMAR DE C° PARA F°:
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 +32
print(monday_temp_f)

#CRIANDO UMA DATAFRAME DE UM DICIONARIO:

data_dicio = {
    "students": ["Benjamim", "Pricila", "Bruno"],
    "scores" : [78, 53, 65]
}  

data_novo = pandas.DataFrame(data_dicio)
print(data_novo)
#CRIAR UM ARQUIVO CSV:
data_novo.to_csv("students_data.csv")