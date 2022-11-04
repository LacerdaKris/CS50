#AMERICAN 15 DIGITOS, INICIO 34 OU 37 - 348282246310005 - 378282246310005
#VISA 13 OU 16 DIGITOS, INICIO 4 - 4312888888881881
#MASTER 16 DIGITOS, INICIO 51, 52, 53, 54 OU 55 - 5405105105105100
from cs50 import get_string
import math
def main():
    cartao = get_string("Numero do cartao: ")
    digito = [int(x) for x in str(cartao)]
    lista1 = []
    lista2 = []
    #conferir se a quantidade de digitos é valida, se sim, qual bandeira:
    if 16 < len(cartao) > 13 or len(cartao) == 14:
        print("INVALID")
    elif digito[0] == 3 and (digito[1] == 4 or 7):
        print("AMEX")
    elif digito[0] == 4:
        print("VISA")
    elif digito[0] == 5 and (digito[1] == 1, 2, 3, 4 or 5):
        print("MASTER")
    else:
        print("INVALID")
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
        getSum(lista2[i])
    print(*lista2)
    print(sum(lista2))
main()

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum
