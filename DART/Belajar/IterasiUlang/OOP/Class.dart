/*
Pembahasan mengenai OOP yang pertama yaitu bagian encapsulation
Enkapsulasi adalah kondisi di mana status atau kondisi di dalam class, dibungkus dan bersifat privat. Artinya objek lain tidak bisa
mengakses atau mengubah nilai dari property secara langsung. Pada contoh kasus kucing kita tidak bisa langsung mengubah berat badan
dari kucing, namun kita bisa menambahkannya melalui fungsi atau method makan.

- Class adalah suatu kelas cara membuatnya yaitu dengan menggunakan tanda kurung kurawal

- Object nah jika kita membahas class tidak bakal jauh dengan yg namanya object, dimana object itu adalah hasil intansiasi dari sebuah
class.
Untuk membuat object kita bisa menggunakan nama class lalu diikuti dengan kurung ()

- Field
Fields / Properties / Attributes adalah data yang bisa kita sisipkan di dalam Object.
Namun sebelum kita bisa memasukkan data di fields, kita harus mendeklarasikan data apa saja yang dimiliki object tersebut di dalam
deklarasi class-nya.
Membuat field sama seperti membuat variable, namun ditempatkan di block class.
Field wajib dimasukkan nilai nya, kecuali field yang nullable.
* Kita juga pada Field dapat di manipulasi loh
Manipulasi Field
Fields yang ada di object, bisa kita manipulasi. Tergantung final atau bukan.
Jika final, berarti kita tidak bisa mengubah data field nya, namun jika tidak, kita bisa mengubah field nya
Untuk memanipulasi data field, sama seperti cara pada variable
Untuk mengakses field, kita butuh kata kunci . (titik) setelah nama object dan diikuti nama field nya

- Method
Selain menambahkan field, kita juga bisa menambahkan method ke object.
Method adalah function yang terdapat di dalam class.
Cara dengan mendeklarasikan method tersebut di dalam block class.
Sama seperti function biasanya, kita juga bisa menambahkan return value, parameter di method yang ada di dalam block class.
Untuk mengakses method tersebut, kita bisa menggunakan tanda titik (.) dan diikuti dengan nama method nya. Sama seperti mengakses
field.
* Method expression Body
Saat membuat method, kadang-kadang kita hanya menggunakan satu baris kode
Jika kita membuat method dengan body yang sangat sederhana, kita bisa gunakan expression body
Expression body mirip seperti ketika kita membuat anonymous function

* Extension Method
Jika kita tidak ingin merubah class yang sudah ada dengan kita menambahkan method, kita bisa buat baris baru cuma baris itu isinya method
yang akan di tambahkan ke class tersebut.
Extension Method adalah cara menambahkan method terhadap Class yang sudah ada, tanpa harus mengubah Class tersebut
Hal ini kadang bermanfaat jika misal Class nya adalah Class milik library yang bukan kita yang membuatnya
Cara menambahkan Extension Method
extension namaExtension on namaClass {
  method yang akan ditambahkan
}

- Operator 
*/

class Person { // => Contoh pembuatan class
  // Contoh pembuatan Field
  String name = "Gentha"; // => Field yang wajib di isi dan kita masukkan nilainya dan dapat di ubah
  String? addresses; // => Field yang tidak wajib diisi, atau istilah lainnya yaitu nullable
  final String country = "Indonesia"; // => Field yang tidak bisa diubah karena dibuat final seperti const cuma ada perbedaan tipis

  // Contoh pembuatan Method pada class Person
  void sayHello(String parameterName){
    print("Hello $name, I am $parameterName"); // Scope jadi name disini pada method bisa di ambil karena masih dalam satu jangkuan
    // yaitu jangkauan di Class Person.
  }
}
// Contoh pembuatan Extension Method
extension GoodByeOnPerson on Person{
  void sayGoodBye(String parameterName){
    print("Goodbye $name in $addresses, From $parameterName");
  }
}

class Computer{
  void startUp() => print("Computer is starting up");
  void shutDown() => print("Computer is shutting down");
  String getInfoComputer() => "This is MacOS"; // => Method expression body
}



void main() {
  var person1 = Person(); // => Contoh object dengan di simpan ke variable
  print(person1);
  Person person = Person(); // Contoh pembuatan object untuk memanggil class Person
  print(person);

  // Memanipulasi Field class Person
  var person2 = Person();
  person2.name = "Ardaana"; // => Pada name kita dapat menggantinya dengan nilai data lain berupa String, ingat karena pada name wajib
  // diisi, Kita tidak bisa memasukan nilai null pada name.
  person2.addresses = "Cibatu"; // => karena addresses nullable, maka kita bisa mengisi nilai nya
  // person.country = "Belanda"; // => Ini tidak bisa dirubah pada country karena dibuat final
  print(person2.name);
  print(person2.addresses);
  print(person2.country);

  // Cara memanggil methodnya
  person2.sayHello("Google");
  // atau cara memanggil method
  Person().sayHello("Siri");
  
  // Cara memanggil method experssion body
  var computer = Computer();
  computer.startUp();
  computer.shutDown();
  print(computer.getInfoComputer());

  // Cara memanggil extension method
  var person3 = Person();
  person3.sayGoodBye("Google");
}
