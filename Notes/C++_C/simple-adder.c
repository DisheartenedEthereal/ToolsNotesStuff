#include <stdio.h>
#include <stdlib.h>


int main(){
    /*
    int num1;
    int num2;
    printf("enter first number: ");
    scanf("%d", &num1);
    printf("enter second number: ");
    scanf("%d", &num2);

    printf("Answer: %d \n", num1 + num2);

    *****

    this calculator is bad cuz it cant add floating point numbers 

    *****
    
    */
    double num1;
    double num2;
    printf("enter first number: ");
    scanf("%lf", &num1);
    printf("enter second number: ");
    scanf("%lf", &num2);

    printf("Answer: %f \n", num1 + num2);


    return 0;
}