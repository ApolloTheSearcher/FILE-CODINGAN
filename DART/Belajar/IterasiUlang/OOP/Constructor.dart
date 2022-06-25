/*
- Constructor
Saat kita membuat Object, maka kita seperti memanggil sebuah method, karena kita menggunakan kurung ().
Di dalam class, kita bisa membuat constructor, constructor adalah method  yang akan dipanggil saat pertama kali Object dibuat.
Mirip seperti di method, kita bisa memberi parameter pada constructor.
Nama constructor harus sama dengan nama class, dan tidak membutuhkan kata kunci void atau return value.
Ketika kita menambahkan Constructor pada class, maka saat membuat Object baru, kita wajib mengikuti parameter yang ada di Constructor.
Di bahasa dart juga kita tidak boleh membuat lebih dari 1 constructor.

- Variable Shadowing
Variable shadowing adalah kejadian ketika kita membuat nama variable dengan nama yang sama di scope yang menutupi variable dengan
nama yang sama di scope diatasnya.
Ini biasa terjadi seperti kita membuat nama parameter di method sama dengan nama field di class.
Saat terjadi variable shadowing, maka secara otomatis variable di scope diatasnya tidak bisa diakses.

- This Keyword
Saat kita membuat kode di dalam block constructor atau method di dalam class, kita bisa menggunakan kata kunci this untuk mengakses
object saat ini.
Misal kadang kita butuh mengakses sebuah field yang namanya sama dengan parameter method, hal ini tidak bisa dilakukan jika langsung
menyebut nama field, kita bisa mengakses nama field tersebut dengan kata kunci this.
This juga tidak hanya digunakan untuk mengakses field milik object saat ini, namun juga bisa digunakan untuk mengakses method.
This bisa digunakan untuk mengatasi masalah variable shadowing, jadi kita bisa menggunakan nama variable yang sama pada constructor
(parameter) dengan nama yang ada field. nama parameter pada constructor dan isi constructor sama denga nama field itu disebut dengan
variable shadowing.

- Initialization Parameter
Kadang saat membuat Constructor, biasanya kita membuat parameter yang hanya digunakan untuk mengubah nilai yang ada di field.
Untuk kasus ini, kita bisa menggunakan fitur Formal Parameter, dimana pada parameter kita bisa langsung sebutkan field mana yang akan 
diubah.
Formal Parameter hanya bisa digunakan di Constructor, tidak bisa digunakan di Method.
Caranya kita cukup ubah parameternya dengan menggunakan this.namaField nya, tanpa perlu menggunakan tipe data.
Jadi kita jika ingin mengubah data di field, kita bisa langsung menggunakan this.namaField pada Constructor parameternya.

- Named constructor
Constructor hanya bisa dibuat satu saja, mirip seperti function atau method, kita tidak bisa membuat beberapa dengan nama yang sama.
Namun terdapat fitur yang bernama Named Constructor, yaitu Constructor dengan nama yang berbeda.
Dengan menggunakan Named Constructor, kita bisa membuat Constructor lebih dari satu, namun wajib menggunakan nama yang berbeda.
Untuk membuatnya kita bisa menggunakan nama Class.namaConstructor nya.
Named Constructor bisa lebih dari satu. tetapi tidak boleh sama namaConstructor dengan Constructor lainnya.
*/
class Person {
  // ↓↓↓↓↓↓↓↓↓↓ => Di bawah ini adalah fieldnya
  String name = "";
  String? addresses;
  final String country = "Indonesia";
  String moto = "";
  String hobby = "";
  int? age;

  // Constructornya ↓↓↓↓↓↓↓↓↓↓
  // Nama constructor harus sama dengan nama class, dan tidak membutuhkan kata kunci void atau return value.
  //                                                       ↓↓↓↓↓↓↓↓↓↓ => Initialization Parameter (This keyword pada parameter)
  Person(String paraName, String paraAddress, String moto, this.hobby) {
    name = paraName; // Disini namenya akan di timpa dengan paraName baru ketika kita membuat object baru
    addresses = paraAddress; // Address juga sama seperti name yang sebelumnya null akan di isi dengan paraAddress ketika membuat
    // object.
    // This Keyword Contoh
    // moto = moto; // kan kalau kaya disamping ini akan terjadi yang namanya itu variable shadowing nah cara mengatasinya dengan this.
    this.moto = moto; // <= Contoh This keyword
  }
  // Contoh variable shadowing
  /*
  Pada variable shadowing itu terjadi jika parameter pada constructor sama dengan nama field di class.
  Sehingga nanti kita menimpanya dengan nama parameter yang ada di constructor. bukan di field jadi nanti menggantinya itu bukan ngambil
  dari field tetapi ngambil dari parameter.
  Person(String name, String addresses){ => Constructor (Contoh variable shadowing)
    name = name; // name disini dia bingung karena name ini dia ngambilnya itu dari field atau dari parameter di constructor
    addresses = addresses; // sama ini juga addresses bingung seperti name
  }
  */
  // Contoh Named Constructor
//↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ => Ini adalah contoh Named Constructor
  Person.agenumber(this.age, String name) {
    //              ⬆️⬆️⬆️⬆️⬆️ => ini adalah contoh Initialization Parameter
    this.name = name; // <= ini adalah contoh This keyword
  }
  Person.addresses( this.addresses); // <= ini adalah contoh Named Constructor sederhana.
  Person.name(String name) {
    this.name = name;
  } //⬆️⬆️⬆️⬆️⬆️ => Contoh named constructor lagi.
  void sayHello(String paraName) {
    print("Hi $name, I am $paraName. My Moto IS $moto, your age is $age");
  }
}

void main(List<String> args) {
  // ↓↓↓↓↓↓↓↓↓↓ => Object baru yang kita buat
  var person1 = Person("Gentha", "Jakarta", "Filosofi Gorengan", "Bermain Basket"); // => karena sudah membuat constructor, 
  // maka kita bisa memanggilnya dengan membuat object
  // baru dan wajib di isi parameter yang ada di constructor
  print(person1);
  Person person = Person("Gentha", "Sukabumi", "Filosofi Gorengan", "Bermain Basket");
  print(person);
  person.sayHello("Google");
  // Cara menggunakan Named Constructor
  /*
  Untuk membuat Object menggunakan Named Constructor, kita bisa langsung mengakses menggunakan Class.namedConstructor()
  */
  var person2 = Person.agenumber(20, "Gentha"); // pemanggilan Named Constructor itu kira harus mengisi parameternya sesuai dengan
  // Named parameter yang kita buat tidak bisa kita mengambil data parameter dari constructor lainnya.
  // karena di constructor Person.agenumber hanya terdapat 2 parameter yaitu age dan name.
  print(person2);
  person2.sayHello("Google"); // Contoh Named Constructor dengan method sayHello
}
