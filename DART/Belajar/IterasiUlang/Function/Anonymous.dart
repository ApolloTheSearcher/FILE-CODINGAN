/*
Anonymous Function
Kebanyakan function biasanya memiliki nama, seperti sayHello(), print() dan  lain-lain.
Kita juga bisa membuat function yang tidak memiliki nama, atau disebut anonymous function.
Di bahasa pemrograman lain ada yang memanggilnya lambda.
Pembuatan anonymous function mirip seperti function bisanya, namun yang membedakan adalah tidak ada nama function nya.
Biasanya anonymous function sering digunakan ketika memanggil function yang membutuhkan parameter berupa function.
Jadi kan sebelumnya kalau kita pakai HighOrderFunction itu terdapat nama function yang kita buat, nah dengan anonymous function ini
kita dapat membuat function yang tidak memiliki nama.
Anonymous function bisa sebagai variable atau parameter
*/
// Anonymous Function as Parameter
void sayHello(String name, String Function(String) filter) {
  var filterName = filter(name);
  print("Hello Nama Saya $filterName");
  print("HI ${filter(name)}"); // => Kalau ini langsung gk mendeklarasikan parameter function filter ke
}

void main() {
  // Inner Function
  // Contoh function biasa bukan anonymous function dengan memiliki nama
  String namaLengkap(String name) {
    // => Function umumnya
    return "Nama Saya $name";
  }

  // Contoh anonymous function
  // Anonymous Function as Variable
  var upperFunction = (String name) {
    // => Anonymous Function
    return name.toUpperCase();
  };
  // ATAU JIKA KITA MENGGUNAKAN SHORT EXPRESSION MENJADI:
  var lowFunction = (String name) => name.toLowerCase();
  // Jadi penjelasan sedikit bahwa di atas ini adalah Anonymous Function. dimana anonymous function yang tidak memiliki nama. functionya
  // Aku simpan kedalam sebuah variable.
  print(upperFunction("Gentha")); // GENTHA
  // atau cara memanggilnya bisa kita deklarasikan dulu
  var result = lowFunction("Gentha");
  print(result); // gentha
  print(namaLengkap("Gentha")); // Nama Saya Gentha
  // Anonymous Function as Parameter ( Contoh nya dengan menggunakan fungsi void sayHello
  //                  ↓↓↓↓ => disini kita tidak usah menggunakan type data String, karena pada function sayHello sudah ada Stringnya.
  sayHello("Gentha Ardaana",(name) => name.toUpperCase()); // Contoh Anonymous Function as Parameter dengan menggunakan Short Expression
  sayHello("Gentha Ardaana", (name) {
    return name.toLowerCase();
  }); // Contoh Anonymous Function as Parameter
  // Jadi Anonymous Function as Parameter yaitu kita langsung membuat function di dalam parameter, keren kan bahasa dart
  // jadi dart kalau function itu bukan hanya sebatas function tapi bisa berupa variable, object , dll.
}
