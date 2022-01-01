#include <iostream>
using namespace std;

int main() {
  int num = 223;
  if(num % 2 == 0)  // % is a modulo-operator, which returns the remainder of a division. on even numbers it will return 0
  {
      cout << "Number is Even"<< endl;
  }else{
    cout << "The number isn\'t even" << endl;
  }
  // Ternary operator
  int age43 = 43;
  bool canIVote = (age43 >= 18) ? true:false;
  cout.setf(ios::boolalpha);
  std::cout << "Can he vote? " << canIVote << std::endl;
  return 0;
}
