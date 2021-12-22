#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, num, sum = 0, temp;
    scanf("%d", &n);
    getchar();
    for (int i = 0; i < n; i++)
    {
        temp = getchar();
        sum += temp - 48;
    }
    printf("%d\n", sum);
    return 0;
}
