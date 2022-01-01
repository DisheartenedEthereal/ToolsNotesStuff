#include <iostream>
using namespace std;

int main() {
  // <type> Name[no of elements];
  int marks[5]; //first we initilize the array by giving it a number and a data type
  //then we can fill the slots
  marks[0] = 96;
  marks[1] = 92;
  marks[2] = 78;
  marks[3] = 54;
  marks[4] = 86;
 // note that this is also possible in a single line
  // int marks[5] = { 96, 92, 78, 54, 86};
  // or even simpler
  // int marks[] = { 96, 92, 78, 54, 86};
  // we can also print it out

  cout << marks[2] << std::endl;
  cout << "We will print also using a for loop" << std::endl;
int i;
  for(int i=0;i<5;i++)
{
  cout<< marks[i] <<endl;  //for printing the i'th element
  cout << "Hey bro" << endl;
	std::cout << "" << std::endl;
}

  return 0;
}
