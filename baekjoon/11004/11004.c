#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b)
{
    if (*(int*)a > *(int*)b)
    {
        return 1;
    }
    else if (*(int*)a < *(int*)b)
    {
        return -1;
    }
    else
    {
        return 0;
    }
}

int main(int argc, char const *argv[])
{
    int n, k;
    int * data;
    scanf("%d %d", &n, &k);
    data = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &data[i]);
    }
    qsort(data, n, sizeof(int), cmp);
    printf("%d", data[k-1]);
    
    return 0;
}
