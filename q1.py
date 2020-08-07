#1 - Faça um código em python3 que leia o arquivo data.csv;

import csv

#Abertura do arquivo de dados na var dados
with open('src/data.csv') as dados:
    
    #Configurando o signo de tabulacao
    leitor = csv.DictReader(dados, delimiter=',')
    
    #Inicia o iterator na primeira linha [cabecario] [dessa forma pula-se a linha com as definicoes de coluna]
    leitor.__next__()
    
    #Iterator para percorrer o arquivo de dados
    for row in leitor:
        print( row )