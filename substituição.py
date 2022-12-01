#criptografa usando uma cifra de substituição, com 26 caracteres do alfabeto como chave.
#exemplo: NQXPOMAFTRHLZGECYJIUWSKDVB - significa que A converte em N, B em Q, etc...
from cs50 import get_string
import string

chave = get_string("Digite a chave com 26 letras: ")
while len(chave) != 26:
    chave = get_string("Digite a chave com 26 letras: ")
digitos = [x for x in str(chave)]
#faz uma lista com as letras do alfabeto:
alfabeto = list(string.ascii_lowercase)
dicionario = {}
n = 0
#inclui ao dicionário cada letra do alfabeto com sua chave correspondente:
for n in range (26):
    dicionario[alfabeto[n]] = digitos[n]
    n += 1

texto = get_string("Digite o texto: ")
cifrado = []
for d in texto:
#se for letra, adiciona o valor da letra (chave no dicionário) em cifrado:
    if d in alfabeto:
        cifrado.append(dicionario.get(d))
#se forem pontuações ou espaços adiciona a lista cifrado (sem alteração):
    else:
        cifrado.append(d)
#"*" imprime todos os itens da lista, e "sep" os separa pelo que for colocado entre aspas.
print("Texto cifrado: ", *cifrado, sep="", end="")
