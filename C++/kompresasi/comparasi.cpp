#include <iostream>
using namespace std;

int main(){
    int a = 1;
    int b = 2;

    bool hasil1, hasil2;


    // komperasi 
    // sebanding
    hasil1 = (a == b);
    cout << hasil1 << endl;
    hasil2 = (a != b);
    cout << hasil2 << endl;

    // kurang dan lebih dari
    hasil1 = (a < b);
    cout << hasil1 << endl;
    hasil2 = (a > b);
    cout << hasil2 << endl;

    // kurang dan lebih dari sama dengan
    hasil1 = (a <= b);
    hasil2 = (a >= b);
    cout << hasil1 <<"\n"<< hasil2 << endl;

    





    return 0;
}