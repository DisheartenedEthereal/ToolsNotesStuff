#include <iostream>
#include <fstream>
#include <sys/ioctl.h>
#include <stdio.h>
#include <unistd.h>
using namespace std;
int getSize(){

    struct winsize w;
    ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);

    printf ("lines %d\n", w.ws_row);
    printf ("columns %d\n", w.ws_col);
		return w.ws_row,w.ws_col;
}
void fetch(){
		std::ifstream f("banner.txt");
		if (f.is_open()){
        std::cout << f.rdbuf();
		}
}
int main()
{
    struct winsize w;
    ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);

    printf ("columns %d\n", w.ws_col);
		fetch();
		std::cout << string("-",w.ws_col) << std::endl;

}
