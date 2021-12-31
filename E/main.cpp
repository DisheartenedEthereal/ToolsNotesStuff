#include <bits/stdc++.h>
#include <stdlib.h>
using namespace std;
void countCurrency(int amount)
{
    int notes[9] = { 100000, 50000, 10000, 5000,
                     2000, 1000, 500, 100, 50 };
    int noteCounter[9] = { 0 };
     
    // count notes using Greedy approach
    for (int i = 0; i < 9; i++) {
        if (amount >= notes[i]) {
            noteCounter[i] = amount / notes[i];
            amount = amount - noteCounter[i] * notes[i];
        }
    }
     
    // Print notes
    cout << "Currency Count ->" << endl;
    for (int i = 0; i < 9; i++) {
        if (noteCounter[i] != 0) {
            cout << notes[i] << " : "
                << noteCounter[i] << endl; }}}
int main (int argc, char *argv[])
{
  if (argc < 2)
  {
    std::cout << "Usage : ./billcounter number" << std::endl;
    return 0;
  } 
    long conv = strtol(argv[1], NULL, 10);
    countCurrency(conv);
    return 0; 
  return 0;
}
