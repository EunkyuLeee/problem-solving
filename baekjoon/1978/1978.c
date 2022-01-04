#define MAX 1000
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
    
    int n, sum = 0, temp;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &temp);
        
        if (primes[temp - 1] == 1)
        {
            sum++;
        }
        
    }
    printf("%d\n", sum);
    
    
    return 0;
}
