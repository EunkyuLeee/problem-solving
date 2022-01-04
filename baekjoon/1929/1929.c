#define MAX 1000000
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int* primes;
    primes = (int*)malloc(sizeof(int) * MAX);
    for (int i = 0; i < MAX; i++)
    {
        primes[i] = 1;
    }
    primes[0] = 0;
    int i = 2, j;
    while (i < (MAX / 2))
    {
        j = 2;
        while (i * j - 1 < MAX)
        {
            primes[i * j - 1] = 0;
            j++;
        }
        i++;
    }
    int m, n;
    scanf("%d %d", &m, &n);
    for (int k = m; k <= n; k++)
    {
        if (primes[k - 1] == 1)
        {
            printf("%d\n", k);
        }
    }
    
    
    return 0;
}
