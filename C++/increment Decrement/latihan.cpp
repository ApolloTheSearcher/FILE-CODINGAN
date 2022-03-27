#include <iostream>
using namespace std;

int main(){
    int a, b;
    cin >> a ;
    b = a;
    cout << "Nilai B pertama adalah " << b << endl;
    b++; // postincrement
    cout << "Nilai B kedua postincrement adalah " << b << endl;
    ++b; // preincrement
    cout << "Nilai B ketiga preincrement adalah " << b << endl;
    b--; // postdecrement
    cout << "Nilai B keempat postdecrement adalah " << b << endl;
    --b; // preincrement
    cout << "Nilai B kelima preincrement adalah " << b << endl;
}