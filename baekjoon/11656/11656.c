#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    char * temp;
    char ** str;
    temp = (char *)malloc(sizeof(char)*100);
    scanf("%s", temp);
    int index = strlen(temp);
    str = (char **)malloc(sizeof(char*)*strlen(temp));
    for (int i = 0; i < index; i++)
    {
        str[i] = (char *)malloc(sizeof(char)*(index-i)+1);
        strcpy(str[i], temp);
        for (int j = 0; j < index; j++)
        {
            temp[j] = temp[j+1];
        }
        
    }
    //free(temp);
    for (int i = 1; i < index; i++)
    {
        for (int j = 0; j < index-i; j++)
        {
            if (strcmp(str[j], str[j+1]) > 0)
            {
                temp = str[j];
                str[j] = str[j+1];
                str[j+1] = temp;
            }
            
        }
        
    }
    for (int i = 0; i < index; i++)
    {
        printf("%s\n", str[i]);
    }
    
    return 0;
}
