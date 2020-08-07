#4 - Salve em um arquivo txt salve o gênero que mais se repete e a idade que mais se repete;

import csv
from collections import Counter

#Lista de dados
lista = []

masculino = 0
feminino = 0

#Abertura do arquivo de dados na var dados
with open('src/data.csv') as dados:
    
    #Configurando o signo de tabulacao
    leitor = csv.DictReader(dados, delimiter=',')
        
    #Iterator para percorrer o arquivo de dados aberto
    cont = 0
    for linha in leitor:  
        #Cria uma lista com as linhas do arquivo de dados
        lista.insert(cont, linha)
        cont += 1 
        
    idades = []
    
    #Conta a quantidade de homems e mulheres na lista ao mesmo tempo que cria uma listagem com as idades
    for i in lista:    
        if (i['gender'] == 'Male'):
            masculino += 1
        else:
            feminino += 1
        
        idades.append(i['age'])
    
    #Cria uma lista com chave sendo a idade repetida e o valor o numero de repeticoes
    idadesCont = Counter(idade for idade in idades)
    
    #Busca a chave com maior valor
    idadeRepetida = max(idadesCont, key=idadesCont.get)
    
    with open('results/results_q4.csv', 'w') as saida:
  
        #Monta as colunas da base de dados
        colunas = ['gender', 'age']
    
        #Vincula o arquivo a um buffer de edicao, configura as conlunas e o delimitador
        maquina = csv.DictWriter(saida, fieldnames = colunas, delimiter = ',', lineterminator = '\n')
        maquina.writeheader()
        
        generoRepetido = ""
        
        #Verifica qual genero repetiu mais
        if (masculino >= feminino):
            generoRepetido = "masculino"
        else:
            generoRepetido = "feminino"
        
        #Escreve a no arquivo de saida os dados lidos da base de dados
        maquina.writerow({'gender': generoRepetido,  'age': idadeRepetida})
        
