#include <stdio.h>

int main(int argc, char const *argv[])
{
    long long a, b, c, d, n;
    scanf("%lld %lld %lld %lld", &a, &b, &c, &d);
    n = b;
    while (n != 0)
    {
        n /= 10;
        a *= 10;
    }
    a += b;
    n = d;
    while (n != 0)
    {
        n /= 10;
        c *= 10;
    }
    c += d;
    printf("%lld\n", a + c);
    return 0;
}
