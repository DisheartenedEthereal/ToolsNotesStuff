#include <stdio.h> 
#include <stdlib.h>
int main() 
{ 
   int age = 30;
   int * pAge = &age; /*A POINTER VARIABLE, STORES &age (ADDRESS OF AGE VARIABLE) */
   printf("Mem address of AGE: %p", &age);
    return 0; 
} 
