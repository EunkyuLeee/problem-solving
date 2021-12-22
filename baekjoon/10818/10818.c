#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, num, max, min;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num);
        if (i == 0)
        {
            max = num;
            min = num;
        }
        else if (max < num)
        {
            max = num;
        }
        else if (min > num)
        {
            min = num;
        }
        
    }
    printf("%d %d\n", min, max);
    return 0;
}
