#include <cstdint>
#include <iostream>

int squareNumbers(int x){ // Declares function "squareNumbers" that takes in parameter of x.
    int y=x*x; //creates int variable equating to x squared
    return y; //returns the value of y when the function is called
}

int main(){
    
    int input = 2555;
    int output = squareNumbers(input);
    std::cout << output << '\n';
    //the function is called, resulting in the int variable "output" equating input squared
}
