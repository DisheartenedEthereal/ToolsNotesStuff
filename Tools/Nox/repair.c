#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int tests(){

    int pass = 0;
    if( access("repair.c", F_OK ) == 0 ) {
    pass = pass+1;} else
    {
        
    }
    
    if( access("dec.c", F_OK ) == 0 ) {
    pass = pass+1;} else
    {
        /* code */
    }
    
    if( access("enc.c", F_OK ) == 0 ) {
    pass = pass+1;}else
    {
        /* code */
    }
    
    if( access("addrhandler.c", F_OK ) == 0 ) {
    pass = pass+1;}else
    {
        /* code */
    }
    
    if( access("runfile.c", F_OK ) == 0 ) {
    pass = pass+1;}else
    {
        /* code */
    }
    
    if( access("addr.nox", F_OK ) == 0 ) {
    pass = pass+1;}else
    {
        /* code */
    }
    

    if (pass == 6)
    {
        return 0;
    }else
    {
        return 1;
    }
    
    
}

int main(){
    int res = tests();
    printf("%d",res);
    return 0;
}