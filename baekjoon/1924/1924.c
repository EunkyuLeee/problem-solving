#include <stdio.h>

int main(int argc, char const *argv[])
{
    int x, y , sum = 0;
    const char* str[7] = {
        "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"
    };
    scanf("%d %d", &x, &y);
    for (int i = 0; i < x; i++)
    {
        if (i == 2)
        {
            sum += 28;
        }
        else if (i == 0){
            continue;
        }
        else if ((i % 2) == 0 && i < 8 || (i % 2) == 1 && i >= 8)
        {
            sum += 30;
        }
        else if ((i % 2) == 0 && i >= 8 || (i % 2) == 1 && i < 8)
        {
            sum += 31;
        }
        
    }
    sum += y;
    printf("%s\n", str[sum%7]);
    return 0;
}
