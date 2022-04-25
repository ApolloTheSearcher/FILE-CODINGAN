/*
Disini kita akan membahas mengenai jenis type data pada bahasa dart sebenarnya setiap bahasa memiliki type data yang sama tetapi
ada sedikit yang baru atau berbeda.
Jenis - Jenis Type data:
- String ("Berupa teks")
- Integer (Berupa angka) int
- Double (Berupa angka dengan desimal) double
- Boolean (Kebenaran) bool
- Num (Bilangan bulat dan desimal) num
- List (Daftar nilai) List
- Map (Pasangan key:value) Map
- dynamic (Semua tipe data)
*/
/*
Kemudian kita selanjut masih mengenai ini disini kita akan membahas mengenai input pada bahasa dart.
pada bahasa dart itu kita input harus mengimportkan terlebih dahulu library yang bernama "dart:io"
Contoh ada pada void main
*/
import 'dart:io'; // <= library yang digunakan untuk input

void main() {
  // Jika masih bingung mengenai dynamic kita beri contoh:
  var namaSaya; // Ini jenis datanya adalah dynamic bukan string jadi kita bebas mau ngisi apa juga type datanya
  namaSaya = "Gentha Ardaana";
  namaSaya = 10;
//↑↑↑↑↑↑↑↑↑↑↑↑↑
// ini gk bakal error karena si variable namaSaya itu type datanya dynamic
  print(namaSaya);
  // Contoh lain
  var kelasSaya = "XI IPA 2";
  // ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
  // Ini jenis type datanya jadi bukan dynamic tetapi jadi string karena nilai isinya string jika kita ganti
  // nilainya jadi angka maka akan error
  // kelasSaya = 10; // Ini akan error
  print(kelasSaya);
  // Cara untuk menambahkan input pada bahasa dart menggunakan stdin.readLineSync()
  // Contoh:
  stdout.write("Masukkan nama kamu: ");
  // ↑↑↑↑↑↑↑↑↑
  // stdout.write hampir sama fungsinya dengan print yaitu menampilkan objek, tetapi stdout.write hanya menampilkan objeknya saja
  // dan ketika ada input atau output baru lagi masih akan ditampilkan di baris yang sama.
  String namaAku = stdin.readLineSync()!;
  //                                  ↑↑↑
  // Tanda operator ! digunakan untuk menandai bahwa input tidak akan mengembalikan nilai null
  stdout.write("Masukkan Umur kamu: ");
  int umurAku = int.parse(stdin.readLineSync()!);
  //            ↑↑↑↑↑↑↑↑↑
  // int.parse ini adalah suatu cara fungsi yang digunakan untuk mengkovert string menjadi integer
  print("Halo $namaAku, umur kamu $umurAku");

  // Disini kita akan membahas mengenai konversi tipe data pada bahasa dart
  // String -> Int
  var sebelas = int.parse("11");
  // String -> Double
  var doubleSebelasKomaDua = double.parse("11.2");
  // Int -> String
  var duabelas = 12.toString();
  // Double -> String
  var piAsString = 3.14159.toStringAsFixed(2); // ini akan menampilkan 3.14
  //                                       ↑ tanda 2 di dalam kurung itu adalah jumlah angka di belakang koma
  print("String ke Int: $sebelas");
  print("String ke Double: $doubleSebelasKomaDua");
  print("Int ke String: $duabelas");
  print("Double ke String: $piAsString");

  // TYPE DATA STRING
  // Perdapat sebuah kasus dimana bagaimana kita jika pada sebuah string terdapat 2 atau lebih tanda petik 2 atau petik 1 jika kita
  // menulis dengan biasa sepertinya akan error, nah solusinya itu dengan menggunakan tanda backslash \ untuk mengurangi ambiguitas
  // dalam tanda petik. Mekanisme ini juga dikenal dengan nama escape string.
  // Contoh:
  print('"I think it\'s great!" I answered confidently');
  // Kemudian bagaimana caranya jika kita ingin membuat suatu string nilai dolar atau mata uang amerika?
  // sedangkan jika kita menggunakan tanda $ di akan secara otomatis akan string expression / formating
  // caranya kita bisa menambahkan huruf r sebelum string, jadi nanti dibacanya sebagai row bukan string
  // Contoh:
  print(r"I have $1 million in the bank");
  //   ↑↑↑ -> huruf r nya
  
}
