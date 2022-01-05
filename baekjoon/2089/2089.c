#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, temp[100], i = 0;
    scanf("%d", &n);
    while (n > 1 || n < 0)
    {
        if (n % (-2) < 0)
        {
            temp[i] = (n % (-2)) + 2;
            n /= (-2);
            n += 1;
        }
        else
        {
            temp[i] = n % (-2);
            n /= (-2);
        }
        i++;
    }
    if (n == 1)
    {
        temp[i] = 1;
        i++;
    }
    if (n == 0)
    {
        temp[i] = 0;
        i++;
    }
    for (i--; i >= 0; i--)
    {
        printf("%d", temp[i]);
    }
    
    return 0;
}
