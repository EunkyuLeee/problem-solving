#include <stdio.h>
#include <stdlib.h>

void sort(int ** data, int size)
{
    int ** left;
    int ** right;
    int temp = size / 2;
    if (size == 1)
    {
        return;
    }
    left = (int**)malloc(sizeof(int*) * temp);
    for (int i = 0; i < temp; i++)
    {
        left[i] = (int*)malloc(sizeof(int) * 2);
    }
    
    right = (int**)malloc(sizeof(int*) * size - temp);
    for (int i = 0; i < size - temp; i++)
    {
        right[i] = (int*)malloc(sizeof(int) * 2);
    }

    for (int i = 0; i < size; i++)
    {
        if (i < temp)
        {
            left[i] = data[i];
        }
        else
        {
            right[i - temp] = data[i];
        }
    }
    sort(left, temp);
    sort(right, size - temp);
    int i = 0, j = 0;
    for (int k = 0; k < size; k++)
    {
        if (i < temp && j < size - temp)
        {
            if (left[i][1] < right[j][1])
            {
                data[k] = left[i];
                i++;
                continue;
            }
            else if (left[i][1] > right[j][1])
            {
                data[k] = right[j];
                j++;
                continue;
            }
        }
        if (i >= temp)
        {
            data[k] = right[j];
            j++;
        }
        else if (j >= size - temp)
        {
            data[k] = left[i];
            i++;
        }
        else
        {
            if (left[i][0] < right[j][0])
            {
                data[k] = left[i];
                i++;
            }
            else if (left[i][0] > right[j][0])
            {
                data[k] = right[j];
                j++;
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    int n;
    int ** data;
    scanf("%d", &n);
    data = (int**)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; i++)
    {
        data[i] = (int*)malloc(sizeof(int) * 2);
        scanf("%d %d", &data[i][0], &data[i][1]);
        
    }
    sort(data, n);
    for (int i = 0; i < n; i++)
    {
        printf("%d %d\n", data[i][0], data[i][1]);
    }
    return 0;
}
