#include <stdio.h>

long long gcd(long long a, long long b);

int main(int argc, char const *argv[])
{
    long long a, b, temp;
    scanf("%lld %lld", &a, &b);
    if (a < b)
    {
        temp = a;
        a = b;
        b = temp;
    }
    temp = gcd(a, b);
    for (long long j = 0; j < temp; j++)
    {
        printf("1");
    }
    
    return 0;
}

long long gcd(long long a, long long b)
{
    long long c = a % b;
    if (c == 0)
    {
        return b;
    }
    else
    {
        return gcd(b, c);
    }
}