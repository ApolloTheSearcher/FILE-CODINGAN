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

// Fungsi dengan return
String perkenalanNamaWithReturn(String nama) {
  return "Nama saya $nama"; // jadi nanti dikembalikan nilai dari fungsi ini
}

// Selain itu bila terdapat sebuah fungsi yang hanya prosesnya itu 1 blok kode atau instruksi kita dapat menyingkatnya dengan menggunakan
// Arrow notasi (=>)
// Contoh :
double average(num num1, num num2) => (num1 + num2) / 2;
void greeting() => print('Hello');

// Kan sebelumnya bahwa sebuah fungsi yang didalamnya terdapat sebuah parameter harus dimasukan inputnya jika ingin menggunakan fungsinya
// nah kita bisa menjadikannya sebagai optional parameter, dimana kita tidak wajib mengisi parameter yang diminta fungsi
// Untuk bisa membuat menjadi optional parameter kita bisa lakukan dengan cara kita memasukannya ke dalam siku saja si parameternya.
// Contoh:
void greetNewUser([String? name, int? age, bool? isVerified]) {
  // Karena sekarang terdapat NULL SAFETY KITA DAPAT MENAMBAKAN TANDA ?
  if (isVerified == true) {
    print('Hello $name, you are $age years old and you are verified');
  } else {
    print('Hello $name, you are $age years old');
  }
}

// Kemudian cara lain pada parameter didalam fungsi bahwa sebelumnya kita harus terurut memasukan parametern yang diminta fungsi
// Disini kita bisa secara acak tidak sesuai urutannya yaitu dengan menggunakan fungsi named parameter dimana nanti kita menggunakan
// tanda kurung kurawal {}.
// required dibawah ini didalam parameter digunakan ketika kita ingin menggunakan parameter yang tidak berurutan. atau kita nanti
// mengisi parameter fungsinya dengan menggunakan type datanya contoh:
// greetNewUser2(age: 20, name: 'Gentha', isVerified: true);
// Contoh:
void greetNewUser2(
    {required String name, required int age, bool isVerified = false}) {
  // Karena sebelumnya nilai sebuah parameternya itu default dan null nah pada named parameternya kita bisa menggunakan required
  if (isVerified == true) {
    print('Hello $name, you are $age years old and you are verified');
  } else {
    print('Hello $name, you are $age years old');
  }
}
