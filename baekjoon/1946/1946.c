#include <stdio.h>

int main(int argc, char const *argv[])
{
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        int n;
        int data[100000][2] = {0};
        int a, b;

        scanf("%d", &n);

        for (int j = 0; j < n; j++)
        {
            scanf("%d %d", &a, &b);
            data[a-1][0] = a;
            data[a-1][1] = b;
        }
        int count = 0;
        int max = data[0][1];
        for (int j = 0; j < n; j++)
        {
            if (data[j][1] <= max)
            {
                count++;
                max = data[j][1];
            }
            
        }
        
        printf("%d\n", count);
    }
    
    return 0;
}
