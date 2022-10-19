#python dna.py small.csv sequences/1.txt
#python dna.py large.csv sequences/6.txt

from csv import reader, DictReader
from sys import argv

if len(argv) < 3:
    print("Sequencia do arquivo: dna.py nome.txt nome.csv")
    exit()

# lê a sequência de dna do arquivo:
with open(argv[2]) as dnafile:
    dnareader = reader(dnafile)
    for row in dnareader:
        dnalist = row

# armazena em uma string:
dna = dnalist[0]
# cria um dicionário onde vamos armazenar as sequências que pretendemos contar:
sequences = {}

# extrai as sequências do banco de dados em uma lista
com open(argv[1]) como arquivo de pessoas:
    people = reader(peoplefile)
    for row in people:
        dnaSequences = row
        dnaSequences.pop(0)
        break

# copia a lista em um dicionário onde os genes são as chaves:
    sequences[item] = 1

# iterar pela sequência de dna, quando encontra repetições dos valores do dicionário de sequências ele as conta
para chave em sequências:
    l = len(key)
    tempMax = 0
    temp = 0
    for i in range(len(dna)):
        # depois de ter contado uma sequência, ela pula no final dela para evitar contar novamente
        enquanto temp > 0:
            temp -= 1
            continue

        # se o segmento de dna corresponder à chave e houver uma repetição dela começamos a contar
        if dna[i:i + l] == chave:
            while dna[i - l: i] == dna[i: i + l]:
                temp += 1
                i += l

            # compara o valor com a sequência mais longa anterior e, se for mais longa, a substitui
            se temp > tempMax:
                tempMax = temp

    # armazena as sequências mais longas no dicionário usando a chave correspondente
    sequences[key] += tempMax

# abre e itera através do banco de dados de pessoas tratando cada um como um dicionário para comparar com as sequências um
com open(argv[1], newline='') como arquivo de pessoas:
    people = DictReader(peoplefile)
    for person in people:
        match = 0
        # compara as sequências com cada pessoa e imprime o nome antes de sair do programa se houver uma correspondência
        for dna in sequences:
            if sequences[dna] == int(person[dna]):
                match += 1
        if match == len(sequences):
            print(person['name'])
            exit()

    print("Não encontrado")
