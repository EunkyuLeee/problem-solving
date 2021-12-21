#include <stdio.h>

int main(int argc, char const *argv[])
{
    int a, b, n;
    char temp;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d %c %d", &a, &temp, &b);
        if (temp == ',')
        {
            printf("%d\n", a+b);
        }
        else
        {
            printf("error!");
            break;
        }
    }
    
    return 0;
}