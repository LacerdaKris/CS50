#A cada ano, nascem 3 lhamas e 4 morrem. Calcular qtos anos p/ popul. final
from cs50 import get_int

inicial = 0
while inicial < 9:
    inicial = get_int("Digite a população inicial(mín.9): ")
final = get_int("Digite a população final: ")
nascidas = inicial/3
mortas = inicial/4
ano = inicial+nascidas-mortas
anos = 1
while ano < final:
    anos += 1
    final = final-ano
print(f"Anos até população final: {anos}")
