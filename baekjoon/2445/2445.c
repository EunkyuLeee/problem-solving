#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        for (int k = 0; k < (n-i)*2; k++)
        {
            printf(" ");
        }
        for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    for (int i = n-1; i >= 0; i--)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        for (int k = 0; k < (n-i)*2; k++)
        {
            printf(" ");
        }
        for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    
    return 0;
}
