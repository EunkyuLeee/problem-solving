#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char s[100];
    int n[26];
    for (int i = 0; i < sizeof(n)/sizeof(int); i++)
    {
        n[i] = -1;
    }
    scanf("%s", s);
    for (int i = 0; i < strlen(s); i++)
    {
        if(n[s[i]-97] == -1)
        {
            n[s[i]-97] = i;
        }
        
    }
    for (int i = 0; i < sizeof(n)/sizeof(int); i++)
    {
        printf("%d ", n[i]);
    }
    
    return 0;
}
