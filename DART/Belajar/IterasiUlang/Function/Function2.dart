/*
- Inner Function
Jadi inner function itu adalah fungsi yang dideklarasikan dalam sebuah fungsi lain. atau di dalam fungsi terdapat fungsi lagi gitu.
Dan itu Inner Function ini hanya bisa di panggil oleh didalam fungsi yang terdapat fungsi inner function.
Atau lebih jelasnya bahwa inner  function yang dibuat di dalam outer function, hanya bisa  diakses dari outer function saja,
tidak bisa diakses dari luar outer function. inner function adalah function yang ada di dalam outer function.

- Main function
Main function adalah fungsi utama pada bahasa dart yang digunakan untuk menjalankan program.
Ternyata main function memiliki parameter optional nya loh yaitu arguments, dimana arguments itu bertipe data List<String>.
Data List<String> tersebut diambil secara otomatis ketika kita menjalankan file dart menggunakan perintah  :
dart namafile.dart arg1 arg2 arg3
dart namafile.dart  "argument 1" "argument  2" "argument 3"

*/
void main(List<String> args) { // Fungsi main adalah outer functionnya
  //      ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ => Parameter optional pada main function. Ini tidak wajib sih diisi.
  // Contoh inner function
  void sayHello(){ // fungsi sayHello adalah inner function
    print("Ini adalah inner function");
  }
  sayHello(); // panggil fungsi sayHello
  // innerFunction(); // Error karena fungsi ini tidak ada di dalam fungsi main
}

// Contoh inner function
void contohOutheFunction(){
  // ignore: unused_element
  void innerFunction(){
    print("Ini adalah inner function");
  } // Nah innerFunction ini hanya dapat di akses di outher function ini, kita tidak bisa mengaksesnya di main function
}