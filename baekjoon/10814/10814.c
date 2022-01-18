#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct person{
    int age;
    char * name;
} per;

void sort(per * data, int size)
{
    per * left;
    per * right;
    int temp = size / 2;
    if (size == 1)
    {
        return;
    }
    left = (per*)malloc(sizeof(per) * temp);
    right = (per*)malloc(sizeof(per) * size - temp);

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
            if (left[i].age <= right[j].age)
            {
                data[k] = left[i];
                i++;
                continue;
            }
            else if (left[i].age > right[j].age)
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
    }
}

int main(int argc, char const *argv[])
{
    int n;
    char temp[100];
    per * data;
    scanf("%d", &n);
    data = (per*)malloc(sizeof(per) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d %s", &data[i].age, temp);
        data[i].name = (char*)malloc(sizeof(char) * (strlen(temp) + 1));
        strcpy(data[i].name, temp);
    }
    sort(data, n);
    for (int i = 0; i < n; i++)
    {
        printf("%d %s\n", data[i].age, data[i].name);
    }
    return 0;
}
