#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct student{
    char * name;
    int kor, eng, math;
} stu;

void sort(stu * data, int size)
{
    stu * left;
    stu * right;
    int temp = size / 2;
    if (size == 1)
    {
        return;
    }
    left = (stu*)malloc(sizeof(stu) * temp);
    right = (stu*)malloc(sizeof(stu) * size - temp);

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
            if (left[i].kor > right[j].kor)
            {
                data[k] = left[i];
                i++;
                continue;
            }
            else if (left[i].kor < right[j].kor)
            {
                data[k] = right[j];
                j++;
                continue;
            }
            else
            {
                if (left[i].eng < right[j].eng)
                {
                    data[k] = left[i];
                    i++;
                    continue;
                }
                else if (left[i].eng > right[j].eng)
                {
                    data[k] = right[j];
                    j++;
                    continue;
                }
                else
                {
                    if (left[i].math > right[j].math)
                    {
                        data[k] = left[i];
                        i++;
                        continue;
                    }
                    else if (left[i].math < right[j].math)
                    {
                        data[k] = right[j];
                        j++;
                        continue;
                    }
                    else
                    {
                        if (strcmp(left[i].name, right[j].name) < 0)
                        {
                            data[k] = left[i];
                            i++;
                            continue;
                        }
                        else if (strcmp(left[i].name, right[j].name) > 0)
                        {
                            data[k] = right[j];
                            j++;
                            continue;
                        }
                    }
                }
                
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
    stu * data;
    scanf("%d", &n);
    data = (stu*)malloc(sizeof(stu) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%s %d %d %d", temp, &data[i].kor, &data[i].eng, &data[i].math);
        data[i].name = (char*)malloc(sizeof(char) * (strlen(temp) + 1));
        strcpy(data[i].name, temp);
    }
    sort(data, n);
    for (int i = 0; i < n; i++)
    {
        printf("%s\n", data[i].name);
    }
    return 0;
}
