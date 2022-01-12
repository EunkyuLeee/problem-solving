#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, m[21];
    scanf("%d", &n);
    m[0] = 0;
    m[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        m[i] = m[i-1] + m[i-2];
    }
    printf("%d\n", m[n]);
    
    return 0;
}
