#include <stdio.h>

int nasty_recursion(int m, int n)
{
    if (m == 0)
    {
        return n + 1;
    }
    else if (m > 0 && n == 0)
    {
        return nasty_recursion(m - 1, 1);
    }
    else
    {
        return nasty_recursion(m - 1, nasty_recursion(m, n - 1));
    }
}

int main()
{
    int result = nasty_recursion(4,4);
    printf("Resultado: %d\n", result);
    return 0;
}