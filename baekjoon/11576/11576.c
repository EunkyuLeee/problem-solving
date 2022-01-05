#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
    int a, b, m, sum = 0, temp;
    scanf("%d %d", &a, &b);
    scanf("%d", &m);
    for (int i = m-1; i >= 0; i--)
    {
        scanf("%d", &temp);
        sum += pow((double)a, (double)i) * temp;
    }
    int val[100], i = 0;
    while (sum > 1)
    {
        val[i] = sum % b;
        sum /= b;
        i++;
    }
    if (sum == 1)
    {
        val[i] = 1;
        i++;
    }
    if (sum == 0)
    {
        val[i] = 0;
    }
    for (i--; i >= 0; i--)
    {
        printf("%d ", val[i]);
    }
    
    return 0;
}