// Contoh pemrograman c++ cara menghitung kuadrat yaitu
// a*x^2 + b*x + c = 0
// didalam program ini kita akan menggunakan rumus kuadrat tapi karena kuadrat kita menggunakan modul cmath 
// Contoh programmnya:
#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int a,b,c;
    cout<<"Enter a:\n";
    cin>>a;
    cout<<"Enter b:\n";
    cin>>b;
    cout<<"Enter c:\n";
    cin>>c;
    /// rumus kuadrat
    double root1,root2;
    root1=(-b+sqrt(b*b-4*a*c)/(2*a));
    root2=(-b-sqrt(b*b-4*a*c)/(2*a));
    cout<<"Root 1 is "<<root1<<"\n";
    cout<<"Root 2 is "<<root2<<"\n";
}