#include <iostream>
// #include <limits>
using namespace std;
int main(){
    int a = 1;
    short b = 2;
    long c = 3;
    long long d = 4;
    float e = 5.0;
    double f = 6.0;
    char g = 'a';
    bool h = false;
    cout << h << endl;
    cout << sizeof(h) << "byte" << endl; // digunakan untuk melihat ukuran dari variable
    cout << numeric_limits <bool>::max() << endl; // digunakan untuk melihat nilai maksimum dari variable
    cout << numeric_limits <bool>::min() << endl; // digunakan untuk melihat nilai minimum dari variable
    return 0;
}