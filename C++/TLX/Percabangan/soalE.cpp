#include <iostream>
using namespace std;

int main(){
    int a;
    cin >> a;
    if (a > 0 && a <= 9){
        cout << "satuan" << endl;
    } else if (a > 9 && a <= 99){
        cout << "puluhan" << endl;
    } else if (a > 99 && a <= 999){
        cout << "ratusan" << endl;
    } else if (a > 999 && a <= 9999){
        cout << "ribuan" << endl;
    } else if (a > 9999 && a < 100000){
        cout << "puluhribuan"<< endl;
    } else {
        cout << "Angka sudah tidak masuk daftar" << endl;
    }
    return 0;
}