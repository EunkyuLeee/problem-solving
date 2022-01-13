#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char temp[100001];
    scanf("%s", temp);

    int stick = 0, piece = 0;
    for (int i = 0; i < strlen(temp); i++)
    {
        if (temp[i] == '(' && temp[i+1] == '(')
        {
            stick++;
        }
        else if (temp[i] == '(' && temp[i+1] == ')')
        {
            piece += stick;
        }
        else if (temp[i] == ')' && temp[i-1] == ')')
        {
            stick--;
            piece++;
        }
    }
    printf("%d\n", piece);
    
    return 0;
}
