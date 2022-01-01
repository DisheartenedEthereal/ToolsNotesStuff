#include <iostream>
#include <vector>
using namespace std;
int main()
{
	std::vector<int> vNums(2);
	vNums[0] = 1;
	vNums[1] = 55;
	vNums.push_back(555);
	std::cout << vNums.size() << std::endl;
	return 0;
}
