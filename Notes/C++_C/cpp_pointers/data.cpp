#include <iostream>
int main()
{	
		int SomeArray[10] = {1,2,3,4,5,6,7,8,9,10};
		int *pLoc = &SomeArray[0];
		for (int i = 0; i < 10; ++i) {
				//std::cout << SomeArray + i << " = "<< *(SomeArray + i) << std::endl;
				std::cout << pLoc << " = " << *pLoc << std::endl;
				pLoc++;
		}

}
