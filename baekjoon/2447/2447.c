#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void star(int a, int x, int y, int ** paint);

int main(int argc, char const *argv[])
{
    int n;
    int ** paint;
    paint = (int **)malloc(sizeof(int*) * (int)pow(3.0, 8.0));
    for (int i = 0; i < (int)pow(3.0, 8.0); i++)
    {
        paint[i] = (int *)malloc(sizeof(int) * (int)pow(3.0, 8.0));
        for (int j = 0; j < (int)pow(3.0, 8.0); j++)
        {
            paint[i][j] = 0;
        }
        
    }
    scanf("%d", &n);
    star(n, 0, 0, paint);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (paint[i][j] == 0)
            {
                printf(" ");
            }
            else
            {
                printf("%c", paint[i][j]);
            }
        }
        printf("\n");        
    }
    
    return 0;
}

void star(int a, int x, int y, int ** paint)
{
    if (a == 3)
    {
        for (int i = 0; i < 3; i++)
        {
            paint[x][y] = '*';
            x += 1;
        }
        x -= 3;
        y += 1;
        paint[x][y] = '*';
        x += 2;
        paint[x][y] = '*';
        x -= 2;
        y += 1;
        for (int i = 0; i < 3; i++)
        {
            paint[x][y] = '*';
            x += 1;
        }
        return;
    }
    else
    {
        int x1, y1;
        x1 = x;
        y1 = y;
        for (int i = 0; i < 3; i++)
        {
            star(a / 3, x1, y1, paint);
            x1 += a / 3;
        }
        x1 -= a;
        y1 += a / 3;
        star(a / 3, x1, y1, paint);
        x1 += a / 3 * 2;
        star(a / 3, x1, y1, paint);
        x1 -= a - a / 3;
        y1 += a / 3;
        for (int i = 0; i < 3; i++)
        {
            star(a / 3, x1, y1, paint);
            x1 += a / 3;
        }
    }
}