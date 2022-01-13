#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    int t;
    char temp[51];
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%s", temp);
        int left = 0, right = 0;
        for (int j = 0; j < strlen(temp); j++)
        {
            if (temp[j] == '(')
            {
                left++;
            }
            else if (temp[j] == ')')
            {
                right++;
            }
            if (left < right)
            {
                break;
            }
        }
        if (left == right)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
        
    }
    
    return 0;
}
