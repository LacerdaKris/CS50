#votação plural, informa número de votos, nomes dos candidatos, e o voto de cada eleitor
#imprime o candidato vencedor (com mais votos), informando inválido se a opção ñ existir

candidatos = {'Alice': 0, 'Bob': 0, 'Charlie': 0}
votos = int(input("Número de votos: "))

for x in range (votos):
    voto = int(input("Digite o número do candidato:\n1 - Alice\n2 - Bob\n3- Charlie\nVoto: "))
    if voto == 1:
        candidatos['Alice'] = candidatos.get('Alice') +1
    elif voto == 2:
        candidatos['Bob'] = candidatos.get('Bob') +1
    elif voto == 3:
        candidatos['Charlie'] = candidatos.get('Charlie') +1
    else:
        while voto != (1, 2 or 3):
            voto = int(input("Voto inválido! Tente novamente: "))

print("O vencedor é: ", max(candidatos, key=candidatos.get))
