#include <iostream>

using namespace std;
const int MAX = 3;

int main () {
   int  var[MAX] = {10, 100, 200};
   int  *ptr;

   // let us have array address in pointer.
   ptr = var;

   for (int i = 0; i < MAX; i++) {
      cout << "Address of var[" << i << "] = ";
      cout << ptr << endl;
// 140731195113176
// 140731195113180
// 140731195113184
      cout << "Value of var[" << i << "] = ";
      cout << *ptr << endl;

      // point to the next location
      ptr++;
   }
   std::cout << "This is for -- operation" << '\n';

   ptr = &var[MAX-1];

  for (int i = MAX; i > 0; i--) {
     cout << "Address of var[" << i << "] = ";
     cout << ptr << endl;
		 cout << "this makes it so " << endl;
     cout << "Value of var[" << i << "] = ";
     cout << *ptr << endl;

     // point to the previous location
     ptr--;
		 cout << "has" << endl;
  }
   return 0;
}
