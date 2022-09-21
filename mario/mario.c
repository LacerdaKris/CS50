#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // solicita numero da altura da pirâmide ao usuário
    int n;
    do
    { 
        n = get_int("Digite um número entre 1 e 8: ");
    }
    while (n < 1 || n > 8);

// for de fora pra linhas e de dentro pra colunas
    for (int i = 0; i < n; i++)
    {
        //espaços em branco
        for (int j = n - 1; j >= i; j--)
         printf (" ");

        // hastes #
        for (int j = 0; j <= i; j++)
        printf ("#");
    printf ("\n");
    }
}
