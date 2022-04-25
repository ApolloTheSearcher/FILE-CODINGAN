// Disini perkenalkan nama saya adalah gentha ardaana dan akan kembali mempelajari ulang mengenai bahasa dart
// Sebelum kita memulai pada bahasa dart, pada dart itu void main() adalah fungsi utama yang akan dijalankan
// dan pada bahasa dart ini sama seperti midle language lainnya.
/*
Pada bahasa dart itu memiliki karakteristik
Statically typed, di mana kita perlu mendefinisikan variabel sebelum bisa menggunakannya.
Type inference, di mana tipe data tidak perlu didefinisikan secara eksplisit. jadi kita hanya menambahkan var didepannya
String expressions, bisa menyisipkan variabel ke dalam sebuah objek String tanpa concantenation (penggabungan objek String
menggunakan tanda +)/ Formating.
Multi-paradigm: OOP & Functional, mendukung konsep object oriented programming dan menggunakan gaya functional programming.
*/
void main(List<String> arguments) {
  // <= Fungsi utama
  // Dibawah ini dia sedang assigment variabel (proses assignment nilai ke variable disebut inisialiasi)
  // ↓↓↓↓↓↓↓↓
  var namaSaya = "Gentha Ardaana"; // <= variabel type inference
  int umurSaya = 17; // <= variabel type inference
  print("Nama saya adalah $namaSaya"); // <= String expression
  print("Umur saya sekarang adalah $umurSaya"); // <= String expression
  print("Hello World");
  // Contoh lain:
  var iniKosong;
  print(iniKosong);
  // Outputnya: null (karena pada dasarnya pada bahasa dart itu setiap deklarasi variable akan memberikan nilai defaultnya yaitu null)
}
