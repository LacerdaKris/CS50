#include <stdio.h>
#include <cs50.h>

//exercício propoe troco apenas com moedas de 25, 10, 5 e 1 centavo
int main(void)
{
    int twentyfive = 0;
    int teen = 0;
    int five = 0;
    int one = 0;
    float recebido = get_float("Digite o valor recebido pelo cliente: \n");
    float compra = get_float("Digite o valor da compra: \n");
    float troco = recebido-compra;
    printf("Troco de: %.2f\n", troco);
    while(troco > 0)
    {
        if(troco >= 0.25)
        {
            twentyfive++;
            troco = troco - 0.25;
        }
        else if(troco >= 0.10)
        {
            teen++;
            troco = troco - 0.10;
        }
        else if(troco >= 0.05)
        {
            five++;
            troco = troco - 0.05;
        }
        else if(troco >= 0.01)
        {
            one++;
            troco = troco - 0.01;
        }
    }
    printf("Sendo...\n %.i moedas de 0,25\n %.i moedas de 0,10\n %.i moedas de 0,05\n %.i moedas de 0,01\n" , twentyfive, teen, five, one);
}
