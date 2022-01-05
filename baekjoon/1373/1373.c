#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX 1000000

int main(int argc, char const *argv[])
{
    int* bin;
    int* oct;
    bin = (int*)malloc(sizeof(int) * (MAX + 1));
    oct = (int*)malloc(sizeof(int) * (MAX / 3));
    int temp, i = 0, k = 0;
    temp = getchar();
    while (temp != EOF && temp != '\n')
    {
        bin[i] = temp - '0';
        i++;
        temp = getchar();
    }
    
    for (i--; i >= 2; i -= 3)
    {
        for (int j = 0; j < 3; j++)
        {
            oct[k] += bin[i-j] * pow((double)2, (double)j);
        }
        k++;
    }
    temp = 0;
    while (i != -1)
    {
        oct[k] += bin[i] * pow((double)2, (double)temp);
        i--;
        temp++;
        if(i == -1)
        {
            k++;
            break;
        }
    }
    
    for (int l = k - 1; l >= 0; l--)
    {
        printf("%d", oct[l]);
    }
    
    return 0;
}
