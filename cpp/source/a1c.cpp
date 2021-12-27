#include <iostream>
using namespace std;

int main()
{
  float bge;
  // let's get the bg reading
  cout << "Enter your blood glucose reading: ";
  cin >> bge;
  // now we run the magic calculation
  float aonec = (bge + 46.7) / 28.7;
  cout << "Your A1C is " << aonec ;
}
// we need to write out the A1C to the database

//

