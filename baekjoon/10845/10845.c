#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    int n, queue[10001], front = 0, back = 0;
    char temp[6];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int x;
        scanf("%s", temp);
        if (!strcmp(temp, "push"))
        {
            scanf("%d", &x);
            queue[back] = x;
            back++;
        }
        else if (!strcmp(temp, "pop"))
        {
            if (front == back)
            {
                printf("-1\n");
            }
            else
            {
                printf("%d\n", queue[front]);
                front++;
            }
        }
        else if (!strcmp(temp, "size"))
        {
            printf("%d\n", back - front);
        }
        else if (!strcmp(temp, "empty"))
        {
            if (front == back)
            {
                printf("1\n");
            }
            else
            {
                printf("0\n");
            }
        }
        else if (!strcmp(temp, "front"))
        {
            if (front == back)
            {
                printf("-1\n");
            }
            else
            {
                printf("%d\n", queue[front]);
            }
        }
        else if (!strcmp(temp, "back"))
        {
            if (front == back)
            {
                printf("-1\n");
            }
            else
            {
                printf("%d\n", queue[back-1]);
            }
        }
    }
    
    return 0;
}
