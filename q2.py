#2 - Salve em um arquivo .csv o first_name e o gender de cada pessoa. E imprima na tela a média das idades;

import csv

#Abertura do arquivo de dados na var dados
with open('src/data.csv') as dados:
    
    #Configurando o signo de tabulacao
    leitor = csv.DictReader(dados, delimiter=',')
    
    #Contados de linhas
    cont = 0
    #Acumulador de idades 
    idades = 0
    
    #Cria o arquivo de saida
    with open('results/results_q2.csv', 'w') as saida:
  
        #Monta as colunas da base de dados
        colunas = ['first_name', 'gender']
    
        #Vincula o arquivo a um buffer de edicao, configura as conlunas e o delimitador
        maquina = csv.DictWriter(saida, fieldnames = colunas, delimiter = ',', lineterminator = '\n')
        maquina.writeheader()
    
        #Iterator para percorrer o arquivo de dados aberto
        for linha in leitor:
            cont += 1
            idades += int(linha['age'])
            
            #Escreve a no arquivo de saida os dados lidos da base de dados
            maquina.writerow({'first_name': linha['first_name'], 'gender': linha['gender']})

print ("media de idades: " + str(idades/cont))