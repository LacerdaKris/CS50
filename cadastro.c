#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    string nome = get_string("Digite seu Nome: ");
    string endereco = get_string("Digite sua Rua/Av e Número: ");
    string cidest = get_string("Digite Cidade e Estado: ");
    printf("Nome: %s\n Endereço: %s\n Cidade: %s\n",nome,endereco,cidest);
}