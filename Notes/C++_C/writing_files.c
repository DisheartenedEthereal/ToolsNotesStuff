#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE * fpointer = fopen("Employees.txt","w");
    fprintf(fpointer, "Mike\nJim"); /*Always Overrides*/


    fclose(fpointer);



    FILE * fpointer2 = fopen("Employees.txt","a");
    fprintf(fpointer2, "\nAppended"); /*Always Appends*/


    fclose(fpointer2);
    FILE * fpointer3 = fopen("ass.txt", "w");
    fprintf(fpointer3, "Hey bro");
    fclose(fpointer3);
    return 0;
}
