#include <iostream>
using namespace std;

int main(){
    int a = 1;
    int b = 2;
    
    bool hasil;
    // and
    hasil = (a == 1) && (b == 2);
    cout << hasil << endl;
    
    hasil = !(a == 2) && (b == 2);
    cout << hasil << endl;

    // or
    hasil = (a == 1) || (b < 2);
    cout << hasil << endl;

    hasil = (a == 2) || (b > 1);
    cout << hasil << endl;

    hasil = (a <= 2) || (b == 2);
    cout << hasil << endl;

}