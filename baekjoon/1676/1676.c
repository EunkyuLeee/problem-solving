#include <stdio.h>

int findnum(int a, int b);

int main(int argc, char const *argv[])
{
    int n, temp, num2 = 0, num5 = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        num2 += findnum(i, 2);
        num5 += findnum(i, 5);
    }
    
    if (num2 < num5)
    {
        printf("%d\n", num2);
    }
    else
    {
        printf("%d\n", num5);
    }
    return 0;
}

int findnum(int a, int b)
{
    int count = 0;
    while (a % b == 0)
    {
        a /= b;
        count++;
    }
    return count;
}