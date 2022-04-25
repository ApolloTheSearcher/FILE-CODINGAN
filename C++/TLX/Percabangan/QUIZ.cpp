#include <iostream>
using namespace std;

int main(){
    int i = 1;
    int n = 10;
    for (int i = 1; i <= n; i++) {
        printf("%d", 2 * i);
}   
    while (i <= 2 * n ){
        printf("%d", i);
        i += 2;
    }
}