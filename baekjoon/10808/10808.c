#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char s[100];
    int n[26] = {0};
    scanf("%s", s);
    for (int i = 0; i < strlen(s); i++)
    {
        n[s[i]-97]++;
    }
    for (int i = 0; i < 26; i++)
    {
        printf("%d ", n[i]);
    }
    
    
    return 0;
}
