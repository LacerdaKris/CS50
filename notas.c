#include <stdio.h>
#include <cs50.h>

int main(void)
{
    float nota1 = get_float("Nota primeiro bimestre: \n");
    float nota2 = get_float("Nota segundo bimestre: \n");
    float media = (nota1+nota2)/2;
    {
        if(media>=6)
        {
            printf("Média:%2f \n Aprovado! \n", media);
        }
        else
        {
            printf("Média:%2f \n Reprovado! \n", media);
        }
    }
}