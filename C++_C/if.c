#include <stdio.h> 
#include <stdlib.h>

int max(int num1,int num2){
    /*
    returns the bigger number between num1 or num2


    */
    int result;
    if (num1 > num2) {
        result = num1;
    }else{
        result = num2;
    }

    return result;

}

int main() 
{ 
    printf("Res: %d", max(51,50)); 
    return 0; 
} 