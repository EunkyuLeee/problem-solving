#include <stdio.h>
#include <stdlib.h>

void sort(long long * data, int size)
{
    long long * left;
    long long * right;
    int temp = size / 2;
    if (size == 1)
    {
        return;
    }
    left = (long long*)malloc(sizeof(long long) * temp);
    right = (long long*)malloc(sizeof(long long) * size - temp);
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
        if (left[i] <= right[j] && i < temp)
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
    int n, max = 0, count = 0;
    long long temp;
    long long * data;
    scanf("%d", &n);
    data = (long long*)malloc(sizeof(long long) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%lld", &data[i]);
    }
    sort(data, n);
    for (int i = 1; i < n; i++)
    {
        for (count = 0; data[i - 1] == data[i]; i++)
        {
            count++;
        }
        if (max < count)
        {
            max = count;
            temp = data[i - 1];
        }
        
    }
    if (max == 0)
    {
        temp = data[0];
    }
    
    printf("%lld\n", temp);
    
    return 0;
}
