#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i < n*2; i++)
    {
        if (i <= n)
        {
            for (int j = 1; j < i; j++)
            {
                printf(" ");
            }
            for (int k = 0; k < (n-i)*2+1; k++)
            {
                printf("*");
            }
            printf("\n");
        }
        else
        {
            for (int j = 1; j < (n*2)-i; j++)
            {
                printf(" ");
            }
            for (int k = 0; k < (i-n)*2+1; k++)
            {
                printf("*");
            }
            printf("\n");
        }
    }
    
    return 0;
}
