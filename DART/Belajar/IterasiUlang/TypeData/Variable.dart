void main() {
  // Disini kita akan membahas mengenai jenis type data yang baru bagi saya di dart yaitu var, final, const, late dan dynamic

  // Pembahasan VAR
  // Var adalah sebuah jenis type data variable dan kita tidak perlu menginisialisasikan type datanya karena dart akan otomatis menentukan type data yang kita buat
  // tetapi harus langsung diinisialisasi
  // Contoh:
  var iniInterger = 10;
  var iniBoolean = true;
  var iniDouble = 10.9;
  var iniString = "ini adalah string";
  print(iniInterger);
  print(iniBoolean);
  print(iniDouble);
  print(iniString);
  // Di atas adalah contoh penggunaan var yang benar
  /*
  Ini adalah contoh yang salah:

  var iniInterger;
  iniInterger = 10;
  // Di atas ini adalah contoh yang salah jika ingin seperti ini kita dapat menggunakan yang namanya dynamic
  // Bukan salah sih tetapi nilainya nanti menjadi sebuah dynamic bukan variable.
  */

  // Pembahasan Final
  // Pada defaultnya sebuah variable pada dart itu bisa dideklarasi ulang, nah bagaimana jika kita
  // tidak ingin mendeklarasikan ulang variablenya, maka kita bisa menggunakan final.
  // Kata kunci final:
  // final tipeData namaVariable = value;
  // final namaVariable = value;
  // Contoh:
  final iniNilaiFinal = 10;
  final iniNamaFinal = "Gentha Ardaana";
  print(iniNilaiFinal);
  print(iniNamaFinal);
  // Jika kita deklarasi ulang di atas dengan nilai lain maka akan error.
  // iniNilaiFinal = 20;
  // iniNamaFinal = "Budi Sastomo";
  // Namun kita dapat merubah isi nilai dari variablenya Contoh:
  final arrayList = [1, 2, 3, 4, 5];
  arrayList[0] = 10;
  // ⬆️⬆️⬆️ disini final tidak akan error karena kita tidak mendeklarasi ulang, tetapi jika kita mendeklarasikan arrayListnya lagi maka
  // akan error
  // arrayList = [10, 20, 30, 40, 50]; // Ini error

  // Pembahasan Const
/*
Const adalah nilai variable yang tidak bisa di ganti dan variablenya tidak bisa dideklarasi ulang (immutable), tetapi apa bedanya dengan final?
Kalo final itu kan agar si variablenya tidak dapat dideklarasi ulang namun nilai dari si variablenya sendiri bisa dirubah.
Const digunakan pada dart itu dijadikan sebuah data Hardcode saat melakukan kompilasi kode program. Jadi hati hati.
Misalkan kita ingin membuat sebuah variable jam nah jika kita menggunakan final maka nilai dari si jam akan mengikuti waktu saat ini,
sedangkan jika kita menggunakan const maka waktunya akan tetap pada saat awal di deklarasikan.
Contoh:
*/
  final array1 = [1, 2, 3, 4, 5];
  const array2 = [1, 2, 3, 4, 5];

  // Maksud final
  // Jika kita buat ulang si array1 maka akan error karena dia menggunakan final, sedangkan hanya merubah isinya tidak akan error.
  // array1 = [0,0,0,0,0]; // INI ERROR KARENA FINAL TIDAK BOLEH DIDEKLARASIKAN ULANG
  array1[3] = 9;
  array2[3] = 9;
  print(array1);
  print(array2); // array2 ini akan error ketika di kompile karena di ubah

  // Pembahasan Late
  // Late adalah sebuah keyword yang digunakan untuk mengatur nilai dari variable yang tidak dideklarasi sebelumnya.
  // Atau kita ingin mengisi variable nya belakangan kita dapat menggunakan late di awal deklarasi variable
  // Contoh:
  var value =
      nama(); // Diakan langsung di eksekusi karena tidak menggunakan late.
  print("Contoh late");
  print(value);
  // ⬆️⬆️⬆️⬆️  Di atas ini adalah cara sederhana memanggil fungsi tetapi nanti urutannya itu pasti akan menampilkan print yang ada di
  // Fungsi nama dulu, kemudian print("Contoh late"), baru nanti akan menampilkan return dari fungsi nama().
  // Tetapi bagaimana kita ingin print("Contoh late") ditampilkan terlebih dahulu?, kita dapat menggunakan late, Contoh:
  late var valueLate =
      nama(); // Jika kita menggunakan late maka dia akan di eksekusi ketika kita memanggil si valueLatenya.
  print("Contoh late diawal");
  print(valueLate);

  // Pembahasan DYNAMIC
  // Pada suatu kasus kita diharuskan membuat variable yang dapat menampung semua jenis type data, pada kasus itu kita dapat menggunakan
  // tipe data dynamic.
  // Contoh:
  dynamic valueDynamic = 10;
  print(valueDynamic);

  valueDynamic = "Diganti menjadi String";
  print(valueDynamic);

  // Kita dapat mengganti isinya dan tipe datanya jika menggunakan dynamic karena dynamic menyimpan semua jenis type data.
  valueDynamic = true;
  print(valueDynamic);
}

// Contoh penggunaan Late
String nama() {
  print("INI FUNGSI NAMA DENGAN MENGGUNAKAN LATE");
  return "Gentha Ardaana";
}
