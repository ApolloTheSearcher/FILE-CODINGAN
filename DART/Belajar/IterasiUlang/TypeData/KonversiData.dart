/*
Bahasa dart adalah bahasa pemrograman yang bersifat objek, dimana semua tipe data dart itu adalah objek. dimana objek memiliki method
dan function
- Konversi number ke string
kita dapat mengkonversi number ke string dengan menggunakan fungsi toString()
- Konversi string ke number
kita dapat mengkonversi string ke number dengan menggunakan method parse() baik berupa int ataupun double
- Konversi number ke number lainnya
kita dapat mengkonversi number ke number lainnya dengan menggunakan method toInt() untuk interger ataupun toDouble() untuk double.
- Konversi Boolean ke String
kita dapat mengkonversi kannya dengan menggunakan method toString().
tetapi untuk mengkonversikan String ke Boolean kita tidak dapat menggunakan method apapun melainkan menggunakan operasi perbandingan.
*/
void main() {
  // Konversi String ke Number
  var inputString =
      "1000"; // hati hati disini ya jika kita isi datanya bukan string angka maka kita tidak dapat mengubahnya ke Number.
  var stringToInt = int.parse(inputString);
  var stringToDouble = double.parse(inputString);

  // Konversi Number ke Numberlainnya
  var intToDouble = stringToInt.toDouble();
  var doubleToInt = stringToDouble.toInt();

  // Konversi Number ke String
  var intToString = stringToInt.toString();
  var doubleToString = stringToDouble.toDouble();

  print(inputString);
  print(stringToInt);
  print(stringToDouble);
  print(intToDouble);
  print(doubleToInt);
  print(intToString);
  print(doubleToString);

  // Konversi Boolean ke String
  var inputBoolean = true;
  var booleanToString = inputBoolean.toString();
  print(booleanToString);

  // Konversi string ke boolean
  // Kita tidak menggunakan method apapun melaikan menggunakan operator perbandingan.
}
