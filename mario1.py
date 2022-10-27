from cs50 import get_int

#Pirâmide, um for pra linhas e outro dentro pra colunas
altura = get_int("Digite uma altura entre 1 e 8: ")
for i in range(altura):
    for j in range(0, altura, 1):
        if i + j < altura - 1:
            print(".", end="")
        else:
            print("#", end="")
    print()
