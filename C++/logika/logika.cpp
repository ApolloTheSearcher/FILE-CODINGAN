#include <iostream>
using namespace std;

int main(){
    int a = 5;
    int b = 2;

    bool hasil;
    // operasi logika = not(negasi), or, and
    // operasi not (negasi)
    cout << "operasi not(negasi) : ";
    hasil = !(a == 7);
    cout << hasil << endl;

    // operasi and
    cout << "operasi and : ";
    hasil = (a == 5) && (b == 2); // True and True = True
    cout << hasil << endl;
    cout << "operasi and : ";
    hasil = (a == 5) && (b == 3); // True and False = False
    cout << hasil << endl;
    hasil = (a == 3) && (b == 2); // False and True = False
    cout << hasil << endl;
    hasil = (a == 3) && (b == 3); // False and False = False

    // operasi or
    cout << "operasi or : ";
    hasil << (a == 5) || (b == 2); // True or True = True
    cout << hasil << endl;
    cout << "operasi or : ";
    hasil << (a == 5) || (b == 3); // True or False = True
    cout << hasil << endl;
    hasil << (a == 3) || (b == 2); // False or True = True 
    cout << hasil << endl;
    hasil << (a == 3) || (b == 3); // False or False = False



}