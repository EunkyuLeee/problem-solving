#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, data[45];
    scanf("%d", &n);
    data[0] = 0;
    data[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        data[i] = data[i-1] + data[i-2];
    }
    printf("%d\n", data[n]);
    return 0;
}
