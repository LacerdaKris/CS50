#criptografa mensagens usando a cifra de César, girando cada letra em posições.
#p é o texto, pi é o i-ésimo caractere em p, e k é uma chave secreta (um inteiro não negativo),
#então cada letra, c i , em o texto cifrado, c , é calculado como: C i = (P i + K)% 26
from cs50 import get_string
from cs50 import get_int

chave = get_int("Digite a chave (número): ")
texto = get_string("Digite o texto: ")
#"ord" converte caracteres em decimal ascii
digitos = [ord(x) for x in str(texto)]
caracter = []
#inclui apenas numero ascii de letras (maiusculas e minusculas)
alfabeto = []
for i in range(65, 123):
    if 64 < i < 91 or 96 < i < 123:
        alfabeto.append(i)
#considera todos os ascii que são letras, soma a chave e adicona a lista caracter
for p in digitos:
    p = int(p)
    if p in alfabeto and p+chave in alfabeto:
        caracter.append(chr(p+chave))
    #se somando a chave fica fora de letras, subtrair a chave
    elif p in alfabeto:
        caracter.append(chr(p-chave))
#se forem pontuações ou espaços adiciona ascii a lista caracter (sem chave pra ficar igual)
    else:
        caracter.append(chr(p))
#"*" imprime todos os itens da lista, e "sep" os separa pelo que for colocado entre aspas.
print("Texto cifrado: ", *caracter, sep="", end="")
