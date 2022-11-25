#Indique os tamanhos solicitados pelos premiados (P ou M)
#Indique quantas camisetas de cada tamanho foram produzidas. 
#Todos os premiados terão a camiseta no tamanho escolhido?

#número total de premiados
N = int(input("Premiados: "))
opcoes = {"1": 0, "2": 0,}

#Solicita que cada premiado escolha o tamanho e soma na opção do dicionário
while N > 0:
    opcao = str(input("Informe 1 para tamanho Pequeno e 2 para Médio: "))
    if opcao == "1":
        opcoes['1'] = opcoes.get('1') +1
    elif opcao == "2":
        opcoes['2'] = opcoes.get('2') +1
    else:
        print("Opção inválida!")
    N -= 1
    
P = int(input("Total P produzidas: "))
M = int(input("Total M produzidas: "))

#Mostra se todos terão o tamanho solicitado (sim ou não)
if P >= opcoes["1"] and M >= opcoes["2"]:
    print("S")
else:
    print("N")
