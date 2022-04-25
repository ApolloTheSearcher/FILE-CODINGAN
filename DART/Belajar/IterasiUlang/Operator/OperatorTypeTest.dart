// Disini kita akan membahas mengenai OperatorTypeTest digunakan untuk mengecek type data
/*
Operator yang digunakan untuk OperatorTypeTest
- as 
TypeCast, melakukan konversi tipe data secara paksa
- is
dia akan menghasilkan true jika object sesuai dengan type data
- is!
dia akan menghasilkan true jika object tidak sesuai dengan type datanya.

=> Biasanya untuk Operator Type Test ini type data diawalnya adalah dynamic
*/
void main(List<String> args) {
  dynamic variable = 10;
  var variablenyaDijadiinInt = variable as int; // Pemaksaan untuk diubah dari dynamic ke interger
  // var variablenyaDijadiinString = variable as String; // Error karena dia bukan string
  // print(variablenyaDijadiinString);
  print(variablenyaDijadiinInt);
  // Mengeceknya
  var isInt = variable is int;
  var isNotBoolean = variable is! bool;
  print(isInt);
  print(isNotBoolean);
}
