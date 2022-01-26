#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int n, k, w, v;
    scanf("%d %d", &n, &k);
    int ** data;
    data = (int**)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; i++)
    {
        data[i] = (int*)malloc(sizeof(int) * k+1);
        for (int j = 0; j <= k; j++)
        {
            data[i][j] = 0;
        }
        
    }
    
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &w, &v);
        if (i == 0)
        {
            for (int j = w; j <= k; j++)
            {
                data[0][j] = v;
            }
        }
        else
        {
            for (int j = 0; j <= k; j++)
            {
                if (w <= j)
                {
                    if (data[i-1][j-w] + v > data[i-1][j])
                    {
                        data[i][j] = data[i-1][j-w] + v;
                    }
                    else
                    {
                        data[i][j] = data[i-1][j];
                    }
                }
                else
                {
                    data[i][j] = data[i-1][j];
                }
            }
        }
    }

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < k+1; j++)
    //     {
    //         printf("%d ", data[i][j]);
    //     }
    //     printf("\n");
    // }
    

    int max = 0;
    for (int i = 0; i <= k; i++)
    {
        if (data[n-1][i] > max)
        {
            max = data[n-1][i];
        }
        
    }
    printf("%d\n", max);
    
    return 0;
}