#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int n, temp;
    int data[10001] = {0};
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &temp);
        data[temp]++;
    }
    for (int i = 0; i < 10001; i++)
    {
        for (int j = 0; j < data[i]; j++)
        {
            printf("%d\n", i);
        }
    }
    
    return 0;
}
