import pandas


#ANALISAR DADOS DO CENTRAL PARK REFERENTE A FAMILIAS DE ESQUILOS E CRIAR DADOS A PARTIR DE SUAS CORES:

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (2).csv") #le oarquivo e o torna um dataframe

#com o dataframe "data" podemos chamar a colna dentro do [] e colocar uma condição e salvar dentro de uma variavél:

squill_gray = len(data[data["Primary Fur Color"] == "Gray"]) #todas as linhas onde na coluna Primary Fur Color for igual a Gray. #"len conta as linhas que possuem o Gray"
squill_black = len(data[data["Primary Fur Color"] == "Black"])
squill_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(squill_gray, squill_black, squill_cinnamon) 

#CRIAR UM DATAFRAME COM BASE NOS DADOS SELECIONADOS:

#criar um dicionario com duas palavras chaves:
dicio_data = {
    "Primary Color": ["Gray", "Black", "Cinnamon"],
    "Count":[squill_gray, squill_black, squill_cinnamon]
}
print(dicio_data)

#com o dicionario podemos tranformar em um dataframe:
df = pandas.DataFrame(dicio_data)
print(df)

#com o dataframe podemos criar um arquivo novo de csv:
df.to_csv("Data_color_squill.csv")

