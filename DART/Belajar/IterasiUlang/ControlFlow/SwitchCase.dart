/*
Pembahasan mengenai Switch Case
Biasanya kita hanya bisa membutuhkan kondisi sederhana di if, seperti hanya menggunakan perbandingan sama dengan (==)
Switch case adalah cara dimana yang digunakan untuk statement percabangan yang sama seperti if, tetapi switch case lebih sederhana
pembuatannya.
Kondisi switch statement hanya untuk perbandingan sama dengan (==).
Contoh:
*/
import "dart:io";

void main() {
  stdout.write("Masukkan nilai : ");
  var nilai = (stdin.readLineSync()!);

  switch (nilai) {
    case "A":
      print("Nilai yang sangat baik pertahankan");
      break;
    case "B":
      print("Nilai yang baik tingkatkan kembali ");
      break;
    case "C":
      print("Nilai yang cukup tingkatkan kembali");
      break;
    case "D":
      print("Nilai yang kurang mengulang kembali");
      break;
    case "F":
      print("Nilai yang sangat kurang mengulang kembali");
      break;
    default:
      print("Masukan nilainya antar A - F");
  }
}
