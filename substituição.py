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
for d in texto:
#transforma todas em minúsculas pra comparar com as chaves do dicionario:
    e = d.lower()
    if e in dicionario:
#se era maiúscula, transformar de volta em letra cifrada e substituir na string(replace):
        if d.isupper():
            texto = texto.replace(f'{d}', f'{(dicionario.get(e)).upper()}')
        else:
            texto = texto.replace(f'{d}', f'{(dicionario.get(e)).lower()}')
print(texto)
        
#Também poderia incluir cada letra cifrada numa lista vazia "cifrado", e depois imprimir
# todos os itens da lista "*"", com "sep" para separar pelo que for colocado entre aspas.
# Exemplo: print("Texto cifrado: ", *cifrado, sep="", end="")
