#include <stdio.h>

int findnum(long long a, long long b);

int main(int argc, char const *argv[])
{
    long long n, m;
    scanf("%lld %lld", &n, &m);
    int sum_2 = 0, sum_5 = 0;
    sum_2 += findnum(n, 2);
    sum_5 += findnum(n, 5);
    sum_2 -= findnum(m, 2);
    sum_5 -= findnum(m, 5);
    sum_2 -= findnum(n-m, 2);
    sum_5 -= findnum(n-m, 5);

    if (sum_2 < sum_5)
    {
        printf("%d\n", sum_2);
    }
    else
    {
        printf("%d\n", sum_5);
    }
    
    return 0;
}

int findnum(long long a, long long b)
{
    int count = 0;
    
    while (a != 0)
    {
        a /= b;
        count += a;
    }
    
    return count;
}