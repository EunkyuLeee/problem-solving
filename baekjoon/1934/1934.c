#include <stdio.h>

int gcd(int a, int b);

int main(int argc, char const *argv[])
{
    int t, a, b, lcm;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &a, &b);
        lcm = a * b / gcd(a, b);
        printf("%d\n", lcm);
    }
    
    return 0;
}
int gcd(int a, int b)
{
    int temp;
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