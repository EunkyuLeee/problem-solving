#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    int n, stack[10000], index = 0;
    char temp[6];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int x;
        scanf("%s", temp);
        if (!strcmp(temp, "push"))
        {
            scanf("%d", &x);
            stack[index] = x;
            index++;
        }
        else if (!strcmp(temp, "pop"))
        {
            if (index == 0)
            {
                printf("-1\n");
            }
            else
            {
                printf("%d\n", stack[index-1]);
                index--;
            }
        }
        else if (!strcmp(temp, "size"))
        {
            printf("%d\n", index);
        }
        else if (!strcmp(temp, "empty"))
        {
            if (index == 0)
            {
                printf("1\n");
            }
            else
            {
                printf("0\n");
            }
        }
        else if (!strcmp(temp, "top"))
        {
            if (index == 0)
            {
                printf("-1\n");
            }
            else
            {
                printf("%d\n", stack[index-1]);
            }
        }
    }
    
    return 0;
}
