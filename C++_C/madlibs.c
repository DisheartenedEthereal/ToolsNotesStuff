#include <stdio.h> 
#include <stdlib.h>

int main(){
    char Color[20];
    char Noun[20];
    char Celeb[20];
    printf("Enter a color: ");
    scanf("%s",Color);
    printf("Enter a noun: ");
    scanf("%s",Noun);
    printf("Enter a Celebrity: ");
    scanf("%s",Celeb);

    printf("\n\n\n");
    printf("Roses are %s\n", Color);
    printf("%ss are blue\n", Noun);
    printf("i love %s\n",Celeb);




}