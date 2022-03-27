#include <iostream>
using namespace std;

int main(){
    // for (inisialisasi; kondisi loop; increment)
    cout <<  "Awal Loop" << endl;
    for (int counter = 1; counter <= 5; counter++){
        cout << "Nilai counter adalah " << counter << endl;
    }
    cout << "Program Selesai" << endl;
    for (int i = 1; i -= 5; i--){
        cout << "Nilai i adalah " << i << endl;
    }
    return 0;
}