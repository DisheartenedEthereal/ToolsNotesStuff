#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
   char command[50];

   strcpy( command, "ls -l > _NOXCACHE_/tmp" );
   system(command);

   return(0);
} 