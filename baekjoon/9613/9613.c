#include <stdio.h>
#include <stdlib.h>

long long gcd(long long a, long long b);

int main(int argc, char const *argv[])
{
    int t, n;
    long long sum;
    long long* input;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d", &n);
        input = (long long*)malloc(sizeof(long long) * n);
        for (int j = 0; j < n; j++)
        {
            scanf("%lld", &input[j]);
        }
        sum = 0;
        for (int j = 0; j < n - 1; j++)
        {
            for (int k = j + 1; k < n; k++)
            {
                sum += gcd(input[j], input[k]);
            }
            
        }
        printf("%lld\n", sum);
    }
    
    return 0;
}

long long gcd(long long a, long long b)
{
    long long temp;
    if (a < b)
    {
        temp = a;
        a = b;
        b = temp;
    }
    for (int i = b; i > 0; i--)
    {
        if (a % i == 0 && b % i == 0)
        {
            return i;
        }
    }
    
}