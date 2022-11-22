#criptografa mensagens usando a cifra de César, girando cada letra em posições.
#p é o texto, pi é o i-ésimo caractere em p, e k é uma chave secreta (um inteiro não negativo),
#então cada letra, c i , em o texto cifrado, c , é calculado como: c i = (p i + k)% 26
from cs50 import get_string
from cs50 import get_int

chave = get_int("Digite a chave (número): ")
texto = get_string("Digite o texto: ")
cifrado = []

for l in texto:
    letras = (int(l) + chave)% 26
    cifrado.append(letras)
    
print(cifrado)
