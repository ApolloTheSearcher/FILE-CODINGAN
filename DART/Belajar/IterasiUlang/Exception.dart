/*
Disini kita akan membahas tentang Exception.
Setiap program yang berjalan mungkin pernah mengalami error atau crash. Kondisi error pada saat program proses / runtime disebut
dengan exception. ketika exception terjadi pada proses maka akan dihentikan dan program selanjutnya juga tidak akan di eksekusi.
Cara mengatasinya kita dapat menggunakan try catch and finally.
- try adalah suatu proses dimana untuk pengujian. dan bilang terdapat exception ketika proses itu kita dapat menambahkan dengan menggunakan
keyword on <nama exception> untuk mengatasi exception tersebut.
- Nah bagaimana jika exception tersebut tidak spesifik, kita dapat menggunakan yang namanya itu catch, dimana kegunaannya untuk menangani
exception yang tidak spesifik.  jadi nanti di dalam catch kita custom untuk pesan exceptionnya.
- Kemudian setelah kita sebelumnya di atas membahas mengenai try dan catch , terdapat satu blok lagi cara yang digunakan untuk menangani
exception handling, yaitu finally, Blok finally akan tetap dijalankan tanpa peduli apa pun hasil yang terjadi pada blok try-catch.
Contoh :
*/

void main() {
  var a = 7;
  var b = 0;
  var c = a ~/ b;
  print(c); // Outputnya akan exception karena pada dasarnya pada matematika kita tidak bisa membagi bilangan lain dengan bilangan nol.
  try {
  var a = 7;
  var b = 0;
  print(a ~/ b);
  // Didalam argument dibawah ini hanya sebagai deklarasi untuk nanti jika ingin di tambahkan pada catch
  //    ↓↓↓↓
} catch(e, s) {
  print('Exception happened: $e');
  print('Stack trace: $s');
// finally akan tetap terus dijalankan tidak peduli pada try and catch tetapi biasanya jika kita menggunakan finally pasti akan ada try.
// ↓↓↓↓↓↓↓
} finally {
  print('This line still executed');
}
}
