#include <iostream>
using namespace std;

int main(){
    int a, b, c;
    cout << "Masukkan nilai a: ";
    cin >> a;
    b = 100;
    cout << "Nilai B adalah " << b << endl;
    b += a;
    cout << "Nilai B ditambah A adalah " << b << endl;
    b -= a;
    cout << "Nilai B dikurang A adalah " << b << endl;
    b *= a;
    cout << "Nilai B dikali A adalah " << b << endl;
    b /= a;
    cout << "Nilai b dibagi A adalah " << b << endl;
    b %= a;
    cout << "Nilai b di modulo A adalah " << b << endl; 
}