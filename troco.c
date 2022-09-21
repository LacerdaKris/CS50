#include <stdio.h>
#include <cs50.h>

//exercício propoe troco apenas com moedas de 25, 10, 5 e 1 centavo
int main(void)
{
    float a = 0.25, b = 0.10, c = 0.05, d = 0.01;
    float recebido = get_float("Digite o valor recebido pelo cliente: \n");
    float compra = get_float("Digite o valor da compra: \n");
    float troco = recebido-compra;
    printf("Troco de: %.2f\n", troco);
    float saldo = troco;
    while(saldo >= 0)
    {
        if(saldo > a)
        {
            saldo = saldo - a;
            printf("Saldo -0,25: %.2f\n", saldo);
        }
        else
        {
            if(saldo > b)
            {
                saldo = saldo - b;
                printf("Saldo -0,10: %.2f\n", saldo);
            }
            else
            {
                if(saldo > c)
                {
                    saldo = saldo - c;
                    printf("Saldo -0,05: %.2f\n", saldo);
                }
                else
                {
                    if(saldo > d)
                    {
                        saldo = saldo - d;
                        printf("Saldo -0,01: %.2f\n", saldo);
                    }
                }
            }
        }
    }

}