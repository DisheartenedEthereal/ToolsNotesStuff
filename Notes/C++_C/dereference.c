#include <stdio.h>
#include <stdlib.h>
int main()
{
    int age = 30;
    int *pAge = &age;
    printf("Address of Age: %p\n",pAge);
    printf("Content of Age's memory address: %d\n",*pAge); /*Dereferenced */
    printf("Content of Age's memory address: %d\n",*&age); /*Dereferenced also possible with *&, stacks infinitely. */
    printf("Content of Age's memory address: %d\n",*&*&*&age);
    return 0;
}
