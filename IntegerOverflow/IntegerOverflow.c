#include <limits.h>
#include <stdio.h>

unsigned int soma(unsigned int a, unsigned int b)
{
    return a + b;
}

int main()
{
    unsigned int a = UINT_MAX;
    unsigned int b = 2;
    printf("A soma é: %d", soma(a, b));
    return 0;
}