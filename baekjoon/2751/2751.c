#include <stdio.h>
#include <stdlib.h>

void sort(int * data, int size)
{
    int * left;
    int * right;
    int temp = size / 2;
    if (size == 1)
    {
        return;
    }
    left = (int*)malloc(sizeof(int) * temp);
    right = (int*)malloc(sizeof(int) * size - temp);
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
        if (left[i] < right[j] && i < temp)
        {
            data[k] = left[i];
            i++;
        }
        else if (left[i] > right[j] && j < size - temp)
        {
            data[k] = right[j];
            j++;
        }
        else if (i >= temp)
        {
            data[k] = right[j];
            j++;
        }
        else if (j >= size - temp)
        {
            data[k] = left[i];
            i++;
        }
    }
    
}

int main(int argc, char const *argv[])
{
    int n;
    int * data;
    scanf("%d", &n);
    data = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &data[i]);
    }
    sort(data, n);
    for (int i = 0; i < n; i++)
    {
        printf("%d\n", data[i]);
    }
    
    return 0;
}
