#Determine qual das 2 palavras vale mais, sendo os pontos conforme lista na ordem do alfabeto
#Ex: "Code" nas regras do Scrabble, C vale 3 pontos, o vale 1, d vale 2 e e vale 1 = 7 pontos.
from cs50 import get_string
import string

#faz uma lista com as letras do alfabeto, e a outra com a pointuação de cada letra:
letras = [chr(x) for x in range(ord('a'), ord('z')+1)]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#função para converter cada letra da palavra em pontos e somar total:
def pontos(p):
    total = 0
    for digit in str(p):
        digit = letras.index(digit.lower())
        total += points[digit]
    return total

def main():
#Solicitar uma palavra de cada jogador:
    palavra1 = get_string("Player 1: ")
    palavra2 = get_string("Player 2: ")
#chama função da pontuação das duas palavras e compara qual é a maior:
    score1 = pontos(palavra1)
    score2 = pontos(palavra2)
    if score1 == score2:
        print("Empate!")
    elif score1 > score2:
        print("Player 1 ganhou!")
    else:
        print("Player 2 ganhou!")
main()
