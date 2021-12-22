#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, sum = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        sum += i;
    }
    printf("%d\n", sum);
    return 0;
}
