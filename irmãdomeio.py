#Insere a idade de 3 irmãs e mostra qual a idade da irmã do meio
idades = []

for a in range(3):
    i = int(input("Idade: "))
    while 5 > i > 100:
        i = int(input("Idade: "))
    idades.append(i)
    
print("Idade da irmã do meio entre as 3 é: ", round(sum(idades)/3))
