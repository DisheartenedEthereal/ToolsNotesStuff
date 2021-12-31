// Some while with continue- and break-statements
#include <iostream>
using namespace std;
int main (void)
{
    int count = 200;  // The start value
    int destination = 0;  // the destination

    // This while will normally terminate when count reaches the destination-value
    while (count > destination) {
        count--;  // decrement count

        if (count == 190) { // If count will turn into 190...
            cout << "skipped..." << endl;
            continue; //... the while-loop will skip to the next iteration due to the "continue"-statement.
        }

        if (count < 180) { // If count falls below 180...
            cout << "aborted..." << endl;
            break; //... the while-loop will be aborted due to the "break"-statement.
        }
        cout << count << endl;  //Note, that this will also execute when target is reached
    }

return 0;
}
