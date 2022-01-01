#include <iostream>
using namespace std;
double cubenumber(double num){


	return num * num * num;
}
int main()
{
	double res = cubenumber(5.0);
	std::cout << res << std::endl;
}
