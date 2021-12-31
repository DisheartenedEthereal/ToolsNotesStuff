#include <stdio.h> 
#include <stdlib.h>

int max(int num1,int num2,int num3){
    /*
    returns the bigger number between num1 or num2


    */
    int result;
    
    if (num1 >= num2 && num1 >= num3) {
        result = num1;
    } else if (num2 >= num1 && num2 >=num3) {
        result= num2;
    } else {
        result= num3;
    }

    return result;

}

int main() 
{ 
    printf("Res: %d", max(51,55,56)); 
    return 0; 
} 