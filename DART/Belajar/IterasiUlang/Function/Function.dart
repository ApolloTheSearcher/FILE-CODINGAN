/*
Disini kita akan membahas mengenai fungsi dimana sebenarnya dari awal kita main dart itu sudah ada fungsi loh
yaitu main() nah main() adalah kumpulan program yang dapat di proses oleh bahasa dart jadi ibaratnya kaya
gerbangnya gitu.
Nah selain main() kita juga dapat membuat fungsi lainnya yaitu dengan menggunakan void dan nama fungsi
- void namaFungsi(){
  // isi fungsi
} tapi jika kita menggunakan void kita tidak menghasilkan output / nilai kembalian (return), biasanya digunakan untuk prosedur.
biasanya jika kita menggunakan void hanya fungsi yang didalamnya mencakup print saja
kita dapat membuat fungsi dengan menggunakan type data yang kita inginkan seperti contoh dibawah ini
returnType functionName(type parameter1, type parameter2){
  // isi fungsi
  return result;
} nah pada fungsi dengan methode ini biasanya dia akan lebih spesifik return hasil nilai dari fungsinya misalnya
jika kita masukan type data double nah jika pada proses terdapat angka desimal yang akan di tampilkan maka
angka desimal tersebut dan typenya double.
- Sebuah fungsi  juga bisa menghasilkan output atau mengembalikan nilai. Fungsi yang mengembalikan nilai ditandai dengan definisi
return type selain void dan memiliki keyword return
*/

// Fungsi main
void main() {
  // Menampilkan dari void perkenalanNama (fungsi) biasa atau tidak menampilkan output atau nilai kembalian
  perkenalanNama("Gentha");
  // Menampilkan dari fungsi perkenalanNamaWithReturn dengan type data String
  // ignore: unused_local_variable
  var namaAku = "Gentha Ardaana";
  var fungsiReturn = perkenalanNamaWithReturn("Gentha Ardaana");
  print("$fungsiReturn");
  // Nah kita bisa bahwa pada fungsi String diatas cara pemanggilannya itu kita harus mendeklarasikannya
  // ke sebuah wadah dulu untuk fungsinya. itu bisa sebut sebagai variable Scope.

  // Contoh menggunakan fungsi void tetapi di parameternya ada yang tidak di deklarasikan jenis type datanya.
  greet("Gentha Ardaana", 2005);


  // Adalah cara pemanggilan fungsi dengan nilai fungsinya null dan fungsi ini menggunakan null safety.
  greetNewUser("Widya", 12, null);
}

// Fungsi biasanya void
void perkenalanNama(String nama) {
  print("Nama saya $nama");
}

// Kemudian jika kita menggunakan void kita juga bisa langsung tanpa mendeklarasikan sebuah type data nya di parameter tetapi
// nantinya kita harus deklarasinya di variable yang lain. Contoh:
void greet(String name, tahunLahir) {
  var umur = 2022 - tahunLahir;
  print("Hallo nama saya $name dan umur saya tahun 2022 adalah $umur tahun.");
}
// Void fungsi itu tidak dapat mengembalikan data menjadi type data yang diinginkan. contoh seperti Int, string dan lain-lain.

// Fungsi dengan return
// Fungsi With Return
String perkenalanNamaWithReturn(String nama) {
  return "Nama saya $nama"; // jadi nanti dikembalikan nilai dari fungsi ini
}
// Jika kita ingin mengembalikan data menjadi type data yang diinginkan maka kita bisa menggunakan fungsi dengan menyebutkan type datanya
// Contoh seperti di atas.

// Function Short Expression
// Selain itu bila terdapat sebuah fungsi yang hanya prosesnya itu 1 blok kode atau instruksi kita dapat menyingkatnya dengan menggunakan
// Arrow notasi (=>)
// Contoh :
double average(num num1, num num2) => (num1 + num2) / 2;
void greeting() => print('Hello');
// Function Short Expression dapat digunakan apabila pada fungsinya sederhana atau satu baris

// - Optional parameter
// Kan sebelumnya bahwa sebuah fungsi yang didalamnya terdapat sebuah parameter harus dimasukan inputnya jika ingin menggunakan fungsinya
// nah kita bisa menjadikannya sebagai optional parameter, dimana kita tidak wajib mengisi parameter yang diminta fungsi
// Untuk bisa membuat menjadi optional parameter kita bisa lakukan dengan cara kita memasukannya ke dalam siku saja si parameternya.
// Atau kita warp si parameter kedalam tanda kurung siku []
// Optional parameter haruslah nullable, atau kita harus menambahkan tanda tanya ? di type datanya.
// Kemudian untuk membuat opsional parameter utamakan parameter yang bukan optional baru parameter optional.
// Jika pada optional parameter temen-temen tidak mau nullable kalian bisa menambahkannya dengan cara default value
// caranya setelah nama parameter, kemudian = default value, kalau pakai default value kita tidak usah lagi menambahkan tanda tanya ?.
// Contoh:                                                  ↓↓↓↓↓↓↓↓↓↓↓↓ => default value String
void greetNewUser(String name, [int? age, bool? isVerified, String email = ""]) {
  // Karena sekarang terdapat NULL SAFETY KITA DAPAT MENAMBAKAN TANDA ?
  if (isVerified == true) {
    print('Hello $name, you are $age years old and you are verified');
  } else {
    print('Hello $name, you are $age years old');
  }
}

// Named parameter

// Kemudian cara lain pada parameter didalam fungsi bahwa sebelumnya kita harus terurut memasukan parametern yang diminta fungsi
// Disini kita bisa secara acak tidak sesuai urutannya yaitu dengan menggunakan fungsi named parameter dimana nanti kita menggunakan
// tanda kurung kurawal {}.
// required dibawah ini didalam parameter digunakan ketika kita ingin menggunakan parameter yang tidak berurutan. atau kita nanti
// mengisi parameter fungsinya dengan menggunakan type datanya contoh:
// greetNewUser2(age: 20, name: 'Gentha', isVerified: true);
// tetapi jika kita menambahkan required kita harus mengisi semua parameter yang diminta fungsi tersebut.
// bagaimana jika kita tidak sengaja mengisi semuanya, kita dapat menggunakan yang namanya itu default parameter value
// caranya simpel kita hanya menambahkan = pada nama parameter dan mengisinya dan tidak menjadikannya nullable.
// Contoh:
void greetNewUser2(
    // ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ => Contoh required parameter tidak menggunakan nullable
    {required String name, required int age, bool isVerified = false}) {
      //                                     ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ => Contoh default parameter value
  // Karena sebelumnya nilai sebuah parameternya itu default dan null nah pada named parameternya kita bisa menggunakan required
  if (isVerified == true) {
    print('Hello $name, you are $age years old and you are verified');
  } else {
    print('Hello $name, you are $age years old');
  }
}
// Atau juga kita bisa membuat named parameter seperti ini menggunakan nullable
void functionNamedParameter({String? name, int? age}){
  print("Perkenalkan nama saya adalah $name dan umur saya adalah $age tahun");
}
// Dengan fungsi di atas kita dapat memanggilnya dengan menggunakan cara berikut:
// functionNamedParameter(name: "Gentha", age: 20); atau juga kita dapat tidak berurutan asalkan kita menyebutkan nama parameternya.



