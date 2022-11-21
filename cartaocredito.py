#AMERICAN 15 DIGITOS, INICIO 34 OU 37 - i: 348282246310005 - v: 378282246310005
#VISA 13 OU 16 DIGITOS, INICIO 4 - i: 4312888888881881 - v: 4003600000000014
#MASTER 16 DIGITOS, INICIO 51, 52, 53, 54 OU 55 - i: 5405105105105100 - v: 5400105005105020
#USAR Algoritmo de Luhn para verificação de validade
from cs50 import get_string
import math
def get_sum(n): # Função para somar os dígitos de um número
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum
def main():
    cartao = get_string("Numero do cartao: ")
    digitos = [int(x) for x in str(cartao)]
    digito = [int(x) for x in str(cartao)]
    lista1 = []
    lista2 = []
#incluir os digitos alternados em 2 listas:
    while (len(digito) != 0):
        ult = digito.pop()
        lista1.append(ult)
        if len(digito) == 0:
            break
        seg_ult = digito.pop()
        lista2.append(seg_ult)
#multiplicar cada item da lista 2 por 2:
    c = len(lista2)
    for i in range(0, c, 1):
        (lista2[i])*=2
        lista2[i]=get_sum(lista2[i])
    total=sum(lista1+lista2)
    ult=str(total)[-1] #último dígito do resultado
#conferir se quantidade de digitos é válida e se o último do total da soma (algoritmo de luhn) é zero, se sim, qual bandeira:
    if 16 < len(cartao) > 13 or len(cartao) == 14 or int(ult) > 0:
        print("INVALID")
    elif digitos[0] == 3 and (digitos[1] == 4 or 7):
        print("AMEX")
    elif digitos[0] == 4:
        print("VISA")
    elif digitos[0] == 5 and (digitos[1] == 1, 2, 3, 4 or 5):
        print("MASTER")
    else:
        print("INVALID")
main()
