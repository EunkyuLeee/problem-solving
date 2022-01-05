#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, b, i = 0, val[100];
    scanf("%d %d", &n, &b);
    while (n > 1)
    {
        val[i] = n % b;
        n /= b;
        i++;
    }
    if (n == 1)
    {
        val[i] = 1;
        i++;
    }
    if (n == 0)
    {
        val[i] = 0;
    }
    for (i--; i >= 0; i--)
    {
        if (val[i] >= 10)
        {
            val[i] -= 10;
            val[i] += 'A';
            printf("%c", val[i]);
        }
        else
        {
            printf("%d", val[i]);
        }
    }
    return 0;
}
