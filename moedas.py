from cs50 import get_float
from sys import argv

#Informar valor da compra, recebido, troco em 25, 10, 5 e 1 centavo.
compra = get_float ("Valor da compra: ")
recebido = get_float ("Valor recebido: ")
troco = recebido - compra
moedas = [{'25': 0}, {'10': 0}, {'5': 0}, {'1': 0}]
if troco > 0.25:
    troco - 0.25
    (moedas[0]) =+1
elif troco > 0.10:
    troco - 0.10
    (moedas[1]) += 1
elif troco > 0.05:
    troco - 0.05
    (moedas[2]) += 1
elif troco > 0.01:
    troco - 0.01
    (moedas[3]) += 1
print("Troco: R$ ", troco)
moeda = (moedas[0])
def f(moeda):
    return (moedas[moeda])
for i in range(0, (moeda+3), 1):
    print(f"{(moeda[i])} moedas de: {(moedas[i])}")
