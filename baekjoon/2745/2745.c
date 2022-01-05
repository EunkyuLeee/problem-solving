#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int* n;
    int b, c, i = 0, sum = 0, temp = 1;
    n = (int*)malloc(sizeof(int) * 1000);
    while ((c = getchar()) != ' ')
    {
        if ('A' <= c && c <= 'Z')
        {
            n[i] = c - 'A' + 10;
        }
        else
        {
            n[i] = c - '0';
        }
        i++;
    }
    scanf("%d", &b);
    for (i--; i >= 0; i--)
    {
        sum += n[i] * temp;
        temp *= b;
    }
    printf("%d\n", sum);
    return 0;
}
