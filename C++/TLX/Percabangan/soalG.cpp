#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int x1, x2, y1, y2;
    cin >> x1 >> x2 >> y1 >> y2;
    if (y1 > x1){
        y1 = y1 - x1;
    } else{
        y1 = x1 - y1;
    }
    if (y2 > x2){
        y2 = y2 - x2;
    } else {
        y2 = x2 - y2;
    }
    cout << y1 + y2 << endl; 
}