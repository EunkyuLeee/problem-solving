#include <stdio.h>

int main(int argc, char const *argv[])
{
    char c;
    int n[4] = {0};
    while((c = getchar()) != EOF)
    {
        if(c != '\n')
        {
            if ('a' <= c && c <= 'z')
            {
                n[0]++;
            }
            else if ('A' <= c && c <= 'Z')
            {
                n[1]++;
            }
            else if ('0' <= c && c <= '9')
            {
                n[2]++;
            }
            else if (c == ' ')
            {
                n[3]++;
            }
        }
        else
        {
            for (int i = 0; i < sizeof(n)/sizeof(int); i++)
            {
                printf("%d ", n[i]);
                n[i] = 0;
            }
            printf("\n");
        }
    }
    return 0;
}
