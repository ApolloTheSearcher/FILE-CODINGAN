/*
Recursive function adalah function yang memanggil function dirinya sendiri.
Kadang dalam pekerjaan, kita sering menemui kasus dimana menggunakan recursive function lebih mudah dibandingkan tidak menggunakan
recursive function.
Contoh kasus yang lebih mudah diselesaikan menggunakan recursive adalah Factorial.

- Namun ketika kita keseringan menggunakan recursiveFunction biasanya terdapat masalah yaitu:
Walaupun recursive function itu sangat menarik, namun kita perlu berhati-hati.
Jika recursive terlalu dalam, maka  akan ada kemungkinan  terjadi error StackOverflow, yaitu error dimana stack pemanggilan function
terlalu banyak.
Kenapa problem ini  bisa terjadi? Karena ketika kita memanggil function, Dart akan menyimpannya dalam stack, jika function tersebut
memanggil function lain, maka stack akan menumpuk terus, dan jika terlalu dalam, maka stack akan terlalu besar, dan bisa menyebabkan
error StackOverflow.

*/
// Fungsi factorial tanpa recursive
int faktorialLooping(int value) {
  int hasil = 1;
  for (var i = 1; i <= value; i++) {
    hasil = hasil * i;
  }
  return hasil;
}

int faktorialRekursiv(int value) {
  if (value == 1) {
    return 1;
  }
  return value * faktorialRekursiv(value - 1);
}

// Contoh masalah dengan recursive function
void loop(int value) {
  if (value == 0) {
    print("Selesai");
  } else {
    print("Looping ke - $value");
    loop(value - 1);
  }
}

void main() {
  // Contoh Faktorial dengan menggunakan Looping
  print(faktorialLooping(5)); // => 120
  // Seperti
  print(1 * 2 * 3 * 4 * 5); // => 120

  // Contoh faktorial dengan menggunakan Recursive Function
  print(faktorialRekursiv(10)); // => 3628800
  // Seperti
  // factorial(10) => 10 * factorial(9) => 9 * factorial(8) => 8 * factorial(7) => 7 * factorial(6) => 6 * factorial(5) => 5 * factorial(4) => 4 * factorial(3) => 3 * factorial(2) => 2 * factorial(1) => 1 * factorial(0) => 1

  // Contoh masalah dengan recursive function
  loop(10000000); // => akan error ketika kita memang memanggilnya dengan data yang cukup besar.
}
