//American Express - 15 dígitos (inicia com 34 ou 37), MasterCard - 16 dígitos (inicia de 51 a 55), Visa - 13 e 16 dígitos (inicia com 4).
//Multiplique cada segundo digito por 2, começando com o penúltimo dígito do número e, em seguida, some os dígitos desses produtos.
//Adicione essa soma à soma dos dígitos que não foram multiplicados por 2.
//Se o último dígito do total for 0, o número é válido!
//Ex:4003600000000014-duplas multiplicar por 2: 1 • 2 + 0 • 2 + 0 • 2 + 0 • 2 + 0 • 2 + 6 • 2 + 0 • 2 + 4 • 2 = 2 + 0 + 0 + 0 + 0 + 12 + 0 + 8
//adicionar os dígitos desses produtos: 2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
//adicionar o resultado à soma dos dígitos que não foram multiplicados por 2 (começando do final): 13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20
// último dígito dessa soma (20) é 0, então o cartão é legítimo!
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long cartao = get_long("Digite número do cartão de crédito: \n");
    //nº de digitos cartão de crédito
    int numDigCreditCard = 0;
    //variáveis necessárias para realizar algoritimo de Luhn
    int digito, digito_, numero_, ultimoDigito, penultimoDigito;
    //contador, partindo do primeiro n° impar
    int i = 1;
    //somatório dos 2 grupos de números (ímpares e pares)
    int digitoImp = 0;
    int digitoPar = 0;
    //string de resposta para usuário
    string output = "";

    //recebe n° do cartão de crédito
    long int creditCard = get_long("Informe o n° do Cartão de Crédito:");

    //obtem n° de dígitos do cartão de crédito
    long int charsCard = creditCard;
    while (charsCard > 0)
    {
        charsCard = round(charsCard / 10);
        numDigCreditCard++;
    }


    //realiza loop aplicando algoritimo de Luhn
    while (creditCard != 0)
    {
        digito = creditCard % 10;

        if (i % 2 == 0)
        {
            numero_ = digito * 2;

            while (numero_ != 0)
            {
                digito_ = numero_ % 10;
                numero_ /= 10;
                digitoPar += digito_;
            }
        }
        else
        {
            digitoImp += digito;
        }

        creditCard /= 10;
        i++;

        penultimoDigito = ultimoDigito;
        ultimoDigito = digito;
    }

    //aplica regra e define se o cartão é valido e qual bandeira pertence
    if ((digitoImp + digitoPar) % 10 != 0)
    {
        output = "INVALID\n";
    }
    else
    {
        if (ultimoDigito == 3 && (penultimoDigito == 4 || penultimoDigito == 7) &&  numDigCreditCard == 15)
        {
            output = "AMEX\n";
        }
        else if (ultimoDigito == 5 && penultimoDigito > 0 && penultimoDigito < 6 &&  numDigCreditCard == 16)
        {
            output = "MASTERCARD\n";
        }
        else if (ultimoDigito == 4 && (numDigCreditCard == 13 || numDigCreditCard == 16))
        {
            output = "VISA\n";
        }
        else
        {
            output = "INVALID\n";
        }

    }
    //exibe para o usuário
    printf("%s", output);
}
