N = int(input("Informe a pressão desejada: "))
M = int(input("Informe a pressão atual: "))

while 1 > N > 40:
    N = int(input("Informe a pressão desejada: "))
    
while 1 > M > 40:
        M = int(input("Informe a pressão atual: "))

print("Diferença: ", N-M)
