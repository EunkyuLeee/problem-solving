#include <stdio.h>

int main(int argc, char const *argv[])
{
    char c;
    char temp;
    c = getchar();
    while (c != EOF && c != '\n')
    {
        if ('A' <= c && c <= 'Z')
        {
            if (c < 'A' + 13)
            {
                c += 13;
            }
            else
            {
                c -= 13;
            }
            putchar(c);
        }
        else if ('a' <= c && c <= 'z')
        {
            if (c < 'a' + 13)
            {
                c += 13;
            }
            else
            {
                c -= 13;
            }
            putchar(c);
        }
        else
        {
            putchar(c);
        }
        c = getchar();
    }
    
    return 0;
}
