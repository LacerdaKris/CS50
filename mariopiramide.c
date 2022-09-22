#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Solicita número ao usuário e repete até ser válido
    int n;
    do
    {
        n = get_int("Número de 1 a 8: \n");
    }
    while(n <+ 1 || n > 8);

    //Pirâmide, um for pra linhas e outro dentro pra colunas
    for(int i = 0; i <= n; i++)
    {
        for(int j = 0; j < n; j++)
        {
                if(i + j > n - 1)
                {
                    printf("#");
                }
                else
                {
                    printf(".");
                }
        }
        for(int j = 0; j < n; j++)
        {
                if(j < i)
                {
                    printf("#");
                }
                else
                {
                    printf(".");
                }
        }
    printf("\n");
    }
}
