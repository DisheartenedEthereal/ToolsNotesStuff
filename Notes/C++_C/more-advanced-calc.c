#include <stdio.h> 
#include <stdlib.h>

double multiply(double num1,double num2){

    return num1 * num2;
}
double divide(double num1, double num2){


    return num1 / num2;
}
double add(double num1, double num2){

    return num1 + num2;

}

double sub(double num1, double num2){
    return num1 - num2;
}

double decider(double num1,double num2,char opr)
    {
    if (opr == '+') {
        return add(num1,num2);
    } else if (opr == '-') {
        return sub(num1,num2);
    } else if (opr == '/') {
        return divide(num1,num2);
    } else {
        return multiply(num1,num2);
    }



}
int main() 
{ 
    double NUM1 ;
    double NUM2 ;
    char OPR;
    printf("Enter number 1 :");
    scanf("%lf",&NUM1);
    printf("Enter number 2 :");
    scanf("%lf",&NUM2);
    printf("Choose operation (+,/,*,-): ");
    scanf(" %c",&OPR);

    printf("Result: %f \n",decider(NUM1,NUM2,OPR));


    return 0; 
} 