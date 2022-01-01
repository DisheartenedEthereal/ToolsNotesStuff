#include <stdio.h> 
#include <stdlib.h>


int main() 
{ 
    int secret_number = 5;
    int guess;
    int tries=0;
    int triesLimit=3;
    int outoftries=0;
    while(guess != secret_number && outoftries == 0){  
        if (tries < triesLimit) {
        
        
        printf("Enter a number: ");
        scanf("%d",&guess);
        tries++;
        } else {
        
             outoftries = 1;
        }
    }
    if (outoftries == 1) {
        printf("U LOSE\n");

    }else {
    printf("U WIN\n");
    }
    return 0; 
} 