/*
Ternary Operator
Cara penulisan code sederhana if statement
Ternary Operator terdiri dari kondisi yang di evaluasi, jika menghasilkan true maka nilai pertama diambil, jika false maka nilai kedua
diambil.
Contoh:
penulisannya itu:
TipeData namaVariable = kondisi ? nilaiPertama : nilaiKedua; => tanda tanya itu adalah if nya atau jika true akan nilai pertama yang
diambil.
*/
void main() {
  // Contoh tidak memakai ternary Operator
  var nilai = 75;
  String ucapan;
  if (nilai >= 75) {
    ucapan = "Lulus";
  } else {
    ucapan = "Tidak Lulus";
  }
  print(ucapan);
  // Contoh menggunakan ternary Operator
  var nilaiUlangan = 80;
  var ucapan1 = nilaiUlangan >= 75 ? "Lulus" : "Tidak Lulus";
  print(ucapan1);
}
