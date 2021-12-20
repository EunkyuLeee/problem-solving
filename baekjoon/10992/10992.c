#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        if (i == n)
        {
            for (int j = 0; j < n*2-1; j++)
            {
                printf("*");
            }
            break;
        }
        else if (i == 1)
        {
            for (int j = 0; j < n-i; j++)
            {
                printf(" ");
            }
            printf("*");
        }
        else
        {
            for (int j = 0; j < n-i; j++)
            {
                printf(" ");
            }
            printf("*");
            for (int k = 0; k < (i-1)*2-1; k++)
            {
                printf(" ");
            }
            printf("*");
        }
        printf("\n");
    }
    
    return 0;
}
