/*
Scope (Disini kita akan membahas mengenai Scope)
Variable atau  Function hanya bisa diakses di dalam area dimana mereka dibuat. Hal ini disebut scope
Contoh, jika sebuah variable dibuat di function, maka hanya bisa diakses di method tersebut, atau jika dibuat didalam block, 
maka hanya bisa diakses didalam block tersebut
*/
void main(){ // Outer function yaitu function main
  // Contoh Scope
  var name = "Gentha"; // Variable yang dibuat di dalam function main
  void sayHello(String name) { // Function yang dibuat di dalam function main (Inner Function)
    var hello = "Hello $name"; // Variable yang dibuat di dalam function sayHello
    print(hello); // => Nah kalau disini tidak akan error karena hello berada di dalam function sayHello dan memanggilnya juga didalam
    // Fungsinya tersebut
  }
  sayHello(name); // Memanggil function sayHello dengan parameter name yang dibuat di dalam function main
  // print(hello) // => ini akan error ketika kita ingin mengakses variable hello di luar jangkauan function sayHello karena hello ini
  // hanya terdapat di dalam function sayHello jadi ketika kita memanggilnya di luar dari fungsi tersebut maka akan terjadi error.
  // Ini yang disebut dengan scope.
}
// Contoh memanggil fuctions yang sudah dibuat di dalam function main dimasukan ke function yang lain
void contoh(){
  // sayHello(); // => ini akan error karena function sayHello() hanya bisa diakses di dalam function main tidak bisa diakses di luar
  // karena function sayHello adalah innerFunction didalam outer function main
}