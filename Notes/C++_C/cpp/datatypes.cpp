#include <iostream>
using namespace std;

int main() {
  typedef int counter; //typedef is basically an alias, u can define int to work as counter as well.

  counter tick_c = 100;  // tick_c is a valid integer variable

  enum colour {red, green, blue} a_colour, another_colour;
  a_colour = green;  // a_colour will be assigned value of '1'
// remember that arrays start from 0

  int foo;
  int bar = 1; // -2,147,483,648 to 2,147,483,647


  int a = 0, b = 1, c = 2, d = 3, e = 4;
  a = b - c + d * e;
  cout << a << endl; // will print 1-2+3*4 = 11

  return 0;
}
