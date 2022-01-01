#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "rwnox.c"
int tests(){

    int pass = 0;
    if( access("repair.c", F_OK ) == 0 ) {
    pass = pass+1;}
    if( access("dec.c", F_OK ) == 0 ) {
    pass = pass+1;}
    if( access("enc.c", F_OK ) == 0 ) {
    pass = pass+1;}
    if( access("addrhandler.c", F_OK ) == 0 ) {
    pass = pass+1;}
    if( access("runfile.c", F_OK ) == 0 ) {
    pass = pass+1;}
    if( access("addr.nox", F_OK ) == 0 ) {
    pass = pass+1;}
    if (pass == 6)
    {
        return 0;
    }else
    {
        return 1;
    }
    
    
}


int main(){
    int gt = tests();
    if (gt == 0)
    {
        printf("Done\n");
    }else
    {
        printf("Not done\n");
    }
    
    



    return 0;
}