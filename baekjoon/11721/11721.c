#include <stdio.h>

int main(int argc, char const *argv[])
{
    char c;
    int i = 0;
    while ((c = getchar()) != EOF)
    {
        if ((i % 10) == 0 && i != 0)
        {
            putchar('\n');
        }
        putchar(c);
        i++;
    }
    
    return 0;
}
