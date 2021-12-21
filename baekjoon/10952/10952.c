#include <stdio.h>

int main(int argc, char const *argv[])
{
    int a, b;
    while (1)
    {
        scanf("%d %d", &a, &b);
        if (a == b && a == 0 && b == 0)
        {
            break;
        }
        printf("%d\n", a+b);
    }
    
    return 0;
}