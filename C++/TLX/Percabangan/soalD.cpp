#include <iostream>
using namespace std;

int main(){
    int a;
    cin >> a;
    if ( a < 0 ){
        cout << "negatif" << endl;
    } else if (a > 0 && a <= 100000){
        cout << "positif" << endl;
    } else if (a == 0){
        cout << "nol" << endl;
    }
    return 0;
}