#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, k, coin[10] = { 0 }, count = 0;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &coin[i]);
    }
    for (int i = n-1; i >= 0; i--)
    {
        if (coin[i] <= k)
        {
            count += k / coin[i];
            k = k % coin[i];
        }
    }
    printf("%d\n", count);
    
    return 0;
}
