#include <stdio.h>

int main(int argc, char const *argv[])
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        int n, max = 0;
        scanf("%d", &n);
        int data[2][100000];
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < n; k++)
            {
                scanf("%d", &data[j][k]);
            }
        }
        if (n == 1)
        {
            if (data[0][0] > data[1][0])
            {
                max = data[0][0];
            }
            else
            {
                max = data[1][0];
            }
        }
        else
        {
            data[0][1] += data[1][0];
            data[1][1] += data[0][0];
            
            for (int k = 2; k < n; k++)
            {
                for (int j = 0; j < 2; j++)
                {
                    if (j == 0)
                    {
                        if (data[j+1][k-1] > data[j+1][k-2])
                        {
                            data[j][k] += data[j+1][k-1];
                        }
                        else
                        {
                            data[j][k] += data[j+1][k-2];
                        }
                    }
                    else
                    {
                        if (data[j-1][k-1] > data[j-1][k-2])
                        {
                            data[j][k] += data[j-1][k-1];
                        }
                        else
                        {
                            data[j][k] += data[j-1][k-2];
                        }
                    }
                }
            }
            
            for (int j = 0; j < 2; j++)
            {
                for (int k = 0; k < n; k++)
                {
                    //printf("%d ", data[j][k]);
                    if (max < data[j][k])
                    {
                        max = data[j][k];
                    }
                }
                //printf("\n");
            }
            
        }
        printf("%d\n", max);
    }
    
    return 0;
}
