/*
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

- Operator didalam class.
Operator adalah method dengan nama yang spesial
Dart memperbolehkan kita membuat method dengan nama operator
Operator yang bisa kita masukan ada banyak seperti:
< , > , <= , >= , == , + , - , * , / , ~/ , % , ~ , & , | , ^ , << , >> , >>>, [], []= 
ini adalah operator yang di perbolehkan untuk membuat operator
* Cara membuat operator
Untuk membuat operator, kita bisa seperti membuat Method, namun nama method diganti menjadi kata kunci operator diikuti dengan operator
nya.
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

// Contoh pembuatan class yang didalamnya terdapat method expression body dimana functionnya seperti function anonymous.
class Computer{
  void startUp() => print("Computer is starting up");
  void shutDown() => print("Computer is shutting down");
  String getInfoComputer() => "This is MacOS"; // => Method expression body
}

// Contoh pembuatan operator pada class Orange
class Orange{
  int quantity = 0;// ↓↓↓↓ => Orange ini adalah dari type data Orange operator yang di awal pada baris 64 jadi nanti waktu di return
  Orange operator + (Orange orange){ // nilai yang di kembalikan berupa Orange.
    var result = Orange(); // => Karena masih scope kita dapat menyimpan terlebih dahulu nilai quantity yang ada di dalam class Orange
    result.quantity = quantity + orange.quantity; // => result.quantity baru dia kemudian di isi sama nilai quantity yang ada di dalam
    // class Orange kemudian di tambahkan dengan quantity yang nanti di isi datanya di void main dengan nilai orange.quantity
    return result; // => Return nilai result nya berupa Orange.
  }
}


void main() {

  // Cara memanggil methodnya
  var person2 = Person(); // => Disini aku simpen dulu si class nya ke dalam variable person2 yang diisi sama class Person()
  person2.sayHello("Google");
  // atau cara memanggil method
  Person().sayHello("Siri"); // => Ini juga cara pemanggilan method tetapi secara langsung gk di simpen kedalam variable
  
  // Cara memanggil method experssion body
  var computer = Computer();
  computer.startUp();
  computer.shutDown();
  print(computer.getInfoComputer());

  // Cara memanggil extension method
  var person3 = Person();
  person3.sayGoodBye("Google");

  // Cara pemanggilan operatornya
  var orange1 = Orange();
  orange1.quantity = 10;
  var orange2 = Orange();
  orange2.quantity = 20; // => disini quantitynya di isi 20 karena pada class Orange kan quantitynya itu 0 kemudian di ganti jadi 20
  // pada orange2.
  // Pemanggunaan operator yang tadi kita buat dibawah ini
  var orange3 = orange1 + orange2; // Uniknya bahasa dart disini kita gk usah menambahkan kembali .quantitiy pada baris ini pada
  // orange 1 dan orange 2.
  // nah jadi kita gk usah lagi pake . kaya gini orange.+(orange2) => ini bakal error, jadi langsung aja karena kita sudah deklarisin
  // si method operator dengan operator + pada class Orange.
  print(orange3.quantity); // => 30 KITA CEK QUANTITY YANG TERBARU.
}
