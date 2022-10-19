#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //em TOTAL o número de notas (arrays) a serem consideradas para cálculo de média.
    int scores[3];
    for (int i = 0; i < 3; i ++)
    {
         scores[i] = get_int("Pontuação:");
    }

    // Calcular média
    float media = (int quantidade, int array[]);
    int soma = 0;
    for (int i = 0; i < quantidade; i++)
    {
        soma += array[i];
    }
    return soma / (float) quantidade;

    printf ("Média: %f \n", media);
}
