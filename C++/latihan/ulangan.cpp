# include <iostream>
using namespace std;

int tri[15][15], i, j;
int main(){
    for (i = 0; i <= 14; i++){
        for (j = 0; j <= 14; j++){
            tri[i][j] = 0;
        }
    }
    tri[0][0] = 1;
    for (i = 1; i <= 14; i++){
        tri[i][0] = 1;
        tri[i][i] = 1;
        for (j = 1; j <= i-1; j++){
            tri[i][j] = tri[i-1][j] + tri[i-1][j-1];
        }
    }
    int sum = 0;
    for (i = 5; i <= 14; i++){
        sum += tri[14][i];
    }
    cout << sum << endl;
    return 0;
}