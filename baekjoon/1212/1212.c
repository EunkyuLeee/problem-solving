#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX 1000000

int main(int argc, char const *argv[])
{
    int* oct;
    int* bin;
    oct = (int*)malloc(sizeof(int) * (MAX / 3 + 2));
    bin = (int*)malloc(sizeof(int) * MAX);
    int temp, i = 0;
    temp = getchar();
    while (temp != EOF && temp != '\n')
    {
        oct[i] = temp - '0';
        i++;
        temp = getchar();
    }
    for (int j = 0; j < i * 3; j++)
    {
        temp = oct[j / 3];
        if (temp >= pow((double)2, (double)(2 - (j % 3))))
        {
            oct[j / 3] -= pow((double)2, (double)(2 - (j % 3)));
            bin[j] = 1;
        }
        else
        {
            bin[j] = 0;
        }
    }
    int isFirst = 1;
    for (int j = 0; j < i * 3; j++)
    {
        if (isFirst == 1)
        {
            if (bin[j] == 0)
            {
                continue;
            }
            else
            {
                isFirst = 0;
                printf("%d", bin[j]);
            }
        }
        else
        {
            printf("%d", bin[j]);
        }
    }
    if (i == 1 && oct[0] == 0)
    {
        printf("0");
    }
    
    return 0;
}
