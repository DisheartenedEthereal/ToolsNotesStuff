#include <cstdio>
#include <iostream>
using namespace std;
double loss(double num1,double num2);
int main()
{
	double numb1 = 0.1111111111111111111111111111111111111111111111;
	double numb2 = 0.1111111111111111111111111111111111111111111111;
	loss(numb1,numb2);
	std::cout << "Hello" << std::endl;
}


double loss(double num1, double num2){

	printf("The sum of two values is %.50f\n", num1 + num2);
	return 0;
}
