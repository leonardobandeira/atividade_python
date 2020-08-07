#3 - Salve em um arquivo .csv o nome completo das últimas 50 pessoas. E imprima alguma informação que você ache interessante;

import csv

#Lista de dados
lista = []

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
        
#Cria o arquivo de saida
    with open('results/results_q3.csv', 'w') as saida:
  
        #Monta as colunas da base de dados
        colunas = ['full_name']
    
        #Vincula o arquivo a um buffer de edicao, configura as conlunas e o delimitador
        maquina = csv.DictWriter(saida, fieldnames = colunas, lineterminator = '\n')
        maquina.writeheader()
        
        #Inverte a lista de tras para frente
        lista.reverse()
        
        #Contador de pessoas maiores de idade
        maiorIdade = 0
        
        i = 0
        while i < 50:
            #Iterator para linha de dados
            linha = lista[i]   
            
            #Verifica idade da pessao atual
            if (int(linha['age']) >= 40):
                maiorIdade += 1
            
            #Escreve o nome completo no documento de saida
            maquina.writerow({"full_name": linha['first_name'] + " " + linha['last_name']})
            i += 1
            
print("Dentre as ultimas 50 pessoas da lista, " + str(maiorIdade) + " sao maiores de 18 anos")