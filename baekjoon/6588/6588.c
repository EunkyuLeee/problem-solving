#include <stdio.h>
#include <stdlib.h>
#define MAX 1000000
int main(int argc, char const *argv[])
{
    
    int* prime;
    prime = (int*)malloc(sizeof(int) * (MAX + 1));
    for (int i = 0; i < (MAX + 1); i++)
    {
        prime[i] = 1;
    }
    prime[0] = 0;
    prime[1] = 0;
    int j = 2;
    while(j <= ((MAX + 1) / 2))
    {
        int k = 2;
        while (j * k < (MAX + 1))
        {
            prime[j * k] = 0;
            k++;
        }
        j++;
    }
    int n;
    scanf("%d", &n);
    while(n != 0)
    {
        for (int i = 2; i < n; i++)
        {
            if (prime[i] == 1 && prime[n - i] == 1)
            {
                printf("%d = %d + %d\n", n, i, n - i);
                break;
            }
            
        }
        scanf("%d", &n);
    }
    
    
    return 0;
}