#criptografa mensagens usando a cifra de César, girando cada letra em posições.
#p é o texto, pi é o i-ésimo caractere em p, e k é uma chave secreta (um inteiro não negativo),
#então cada letra, c i , em o texto cifrado, c , é calculado como: c i = (p i + k)% 26
from cs50 import get_string
from cs50 import get_int

chave = get_int("Digite a chave (número): ")
texto = get_string("Digite o texto: ")
digitos = []
caracter = range(len(texto)+1)
        
for i in caracter:
#converte letras e números no decimal ascii com a chave somada e adicona a lista digitos
    if 123 > i > 64 or 58 > i > 47:
        ascii = ord(texto[i])+chave
        digitos.append(ascii)
#traduz pontuacoes em decimal ascii e adiciona a lista digitos
    else:
        digitos.append(i)
    
    print(chr(digitos[i]))
