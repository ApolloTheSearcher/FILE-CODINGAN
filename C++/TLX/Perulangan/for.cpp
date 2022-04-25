#include <iostream>
using namespace std;


int main() {
    int N, Bi, hasil;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> Bi;
        hasil += Bi;
    }
    cout << hasil << endl;
    return 0;
}