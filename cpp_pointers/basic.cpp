#include <iostream>
using namespace std;
int main()
{
		int SomeArray[10];
		int *pLocation = &SomeArray[6];
		int *pLocation2 = &SomeArray[0];
		std::cout << "Pointer one: " << pLocation << std::endl;
		std::cout << "Pointer two: " << pLocation2 << std::endl;
		std::cout << "Differnce: " << pLocation - pLocation2 << std::endl;
		return 0;
}
