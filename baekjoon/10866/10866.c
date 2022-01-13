#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    int n, deque[20001], front = 10000, back = 10000;
    char temp[11];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int x;
        scanf("%s", temp);
        if (!strcmp(temp, "push_front"))
        {
            scanf("%d", &x);
            deque[front-1] = x;
            front--;
        }
        else if (!strcmp(temp, "push_back"))
        {
            scanf("%d", &x);
            deque[back] = x;
            back++;
        }
        else if (!strcmp(temp, "pop_front"))
        {
            if (front == back)
            {
                printf("-1\n");
            }
            else
            {
                printf("%d\n", deque[front]);
                front++;
            }
        }
        else if (!strcmp(temp, "pop_back"))
        {
            if (front == back)
            {
                printf("-1\n");
            }
            else
            {
                printf("%d\n", deque[back-1]);
                back--;
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
                printf("%d\n", deque[front]);
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
                printf("%d\n", deque[back-1]);
            }
        }
    }
    
    return 0;
}
