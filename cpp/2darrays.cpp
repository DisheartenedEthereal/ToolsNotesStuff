#include <iostream>
int main()
{
	int numberGrid[3][2] = {

												{1,2},
												{3,4},
												{5,6}
	};
	int darray[2][4]{
		{}
		{}
		{}
		{}

	};
	for (int n = 0; n < 3; n++) {
		for (int y = 0; y < 2; y++) {
			std::cout << numberGrid[n][y] ;

		} /* for (; ; var++) */
	std::cout << std::endl;
	} /* for (; ; var++) */
	return 0;
}
