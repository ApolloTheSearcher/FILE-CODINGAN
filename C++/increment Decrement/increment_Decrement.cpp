#include <iostream>
using namespace std;

int main(){
    // Increment dan Decrement
    // Increment adalah penambahan variable sebanyak 1 angka
    // postincrement adalah menambahkan nilai variable sebanyak 1 angka
    int a, b;
    a = 2;
    cout << "Nilai A awal adalah " << a << endl;
    a++; // postincrement
    cout << "Nilai A Increment adalah " << a << endl;
    // preincremen
    b = 9;
    cout << "Nilai B awal adalah " << b << endl;
    ++b; // preincrement
    cout << "Nilai B Precrement adalah " << b << endl;

    // Decrement adalah pengurangan variable sebanyak 1 angka
    int c, d;
    c = 10;
    cout << "Nilai C awal adalah " << c << endl;
    c--; // postdecrement
    cout << "Nilai C Decrement adalah " << c << endl;
    // predecrement
    d = 5;
    cout << "Nilai D awal adalah " << d << endl;
    --d;
    cout << "Nilai D PreDecrement adalah " << d << endl;
}