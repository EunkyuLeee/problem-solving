#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, fibo, n1, n2, temp;
    scanf("%d", &n);
    n2 = 0;
    n1 = 0;
    for (int i = 0; i <= n; i++)
    {
        temp = n2;
        n2 = n1;
        n1 += temp;
        if (i == 2)
        {
            n1 = 1;
        }
        
    }
    printf("%d\n", n1 + n2);
    return 0;
}