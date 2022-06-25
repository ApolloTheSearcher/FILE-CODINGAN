/*
Pembahasan mengenai Null Safety pada dart terbaru di atas version 2.12
Biasanya pada bahasa pemrograman yang lain, bahwa setiap programmer pasti akan pernah merasakan kesalahan tersebut.
Yaitu NullPointerException. dimana ini terjadi ketika kita mengakses sebuah data, ternyata data tersebut adalah null.
Nah Dart mendukung terhadap Null Safety, jadi akan lebih membantu ketika terjadi kesalahan mengakses data yang bisa null.

- Null Check
Secara default, saat kita akan mengakses property, method atau operator terhadap data yang nullable (bisa null),
maka Dart akan memberi compile error
Dart akan meminta kita melakukan Null Check terlebih dahulu, sebelum mengakses data nullable nya.

- Konversi nullable ke non nullable
Jika kita ingin melakukan konversi non nullable ke nullable, maka kita dapat langsung saja memasukan datanya saja.
Sedangkan jika kita ingin melakukan konversi nullable ke non nullable, kita wajib melakukan null check terlebih dahulu.

- Default Value
Kadang kita butuh melakukan konversi dari tipe data nullable ke non nullable, namun jika data nya ternyata null,
kita ganti dengan default value
Untuk melakukan hal tersebut, kita tidak  perlu menggunakan if else, kita cukup  menggunakan operator ??  (tanda tanya dua kali)

- Konversi secara paksa
Dart mendukung konversi secara paksa dari tipe data nullable ke non nullable dengan menggunakan karakter ! (tanda seru) setelah nama
variable nullable nya.
Namun konsekuensinya, jika ternyata datanya  null, maka otomatis akan terjadi error ketika aplikasi berjalan, jadi gunakan secara
bijak. Jadi ini digunakan kalau kita memang sudah pasti bahwa datanya itu tidak null. jangan sampai samar - samar.

- Mengakses Nullable Member
Saat kita mengakses nullable member (property, method, operator), maka secara default Dart akan memberi  peringatan untuk melakukan
null check.
Namun Kita bisa mengakses nullable member secara aman, tanpa harus memaksa melakukan konversi, caranya dengan menggunakan tanda tanya
(?).
Namun konsekuensinya, ketika mengakses nullable member, hasil dari member tersebut bisa jadi null kalo datanya ternyata null
Jadi harus dipastikan ya karena jika kita mengisinya dengan data null maka nanti hasilnya akan null dan lier.

*/
void main(List<String> args) {
  // Null Check
  int? nilai = null; //    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ => Null Check akan error
  // double nilaiDesimal = nilai.toDouble();// Nah ini berpotensi NullPointerException karena nilai adalah null,
  // disini fungsinya null check. ↑↑↑↑↑↑
  // Nah bagaimana cara mengatasinya yaitu kita bisa menggunakan if statement seperti ini:
  if (nilai != null) {
    double nilaiDesimal = nilai.toDouble();
    print(nilaiDesimal);
  } // Mengatasi NullPointerException dengan menggunakan if statement. (Null Check).

  // Konversi non nullable to nullable
  String nama = "Gentha";
  String? nullableName = nama; // => Konversi non nullable ke nullable
  print(nullableName);

  // Konversi nullable to non nullable
  int? nullableInt;
  if (nullableInt != null) {
    int number =
        nullableInt; // => jika kita ingin mengkonversi nullable ke non nullable, seperti contoh di garis ini. masukan data
    // NullableInt yang nullabel ke variable number yang non nullable. dengan menggunakan null check terlebih dahulu.
    print(number);
  } // => Konversi nullable ke non nullable dengan menggunakan null check.

  // Default Value
  String? nullableint;
  var numberDefault = nullableint ?? "Number"; // => Default Value
  print(numberDefault);
  // Di atas adalah cara sederhana untuk merubah data nullable menjadi non nullable dengan menggunakan operator ??
  // Sebelumnya kita harus menggunakan if statement untuk mengecek apakah data nullable atau tidak.
  // atau kita juga dapat menggunakan ternary operator untuk mengecek apakah data nullable atau tidak.
  String numberDefaultTernary = nullableint != null ? nullableint : "Non nullable dengan ternary operator";
  print(numberDefaultTernary);

  // Konversi secara paksa
  String? nullablePaksa;
  // nullablePaksa = "Gentha"; // => kita bisa mengatasi errornya dengan memberikan nilai ke variable nullablePaksa.
  String nonNullablePaksa = nullablePaksa!; // => Konversi secara paksa dengan menggunakan tanda !, tapi diingat bahwa ini kita sudah
  // pasti bahwa data nullable nya tidak null.
  print(nonNullablePaksa); // error karena nilai dari nullablePaksa adalah null.

  // Mengakses Nullable Member
  int? nilaiMember;
  double? nilaiMemberDesimal = nilaiMember?.toDouble(); // => Mengakses nullable member dengan menggunakan tanda tanya.
  print(nilaiMemberDesimal); // => Outputnya null. karena kita tidak mengisi apa apa di variable nilaiMember jadi secara default null.
  // Ini paling biasanya digunakan untuk input dan output data
  // Jika kita ingin mengakses method, property, atau operator kita bisa menambahkan tanda tanya(?) seperti contoh di atas.

}
