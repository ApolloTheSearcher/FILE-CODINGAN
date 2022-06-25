/*
- Named constructor
Constructor hanya bisa dibuat satu saja, mirip seperti function atau method, kita tidak bisa membuat beberapa dengan nama yang sama.
Namun terdapat fitur yang bernama Named Constructor, yaitu Constructor dengan nama yang berbeda.
Dengan menggunakan Named Constructor, kita bisa membuat Constructor lebih dari satu, namun wajib menggunakan nama yang berbeda.
Untuk membuatnya kita bisa menggunakan nama Class.namaConstructor nya.
Named Constructor bisa lebih dari satu. tetapi tidak boleh sama namaConstructor dengan Constructor lainnya.

- Redirecting Constructor
Saat membuat Named Constructor, kita bisa memanggil Default Constructor, atau istilahnya adalah melakukan Redirecting Constructor.
Cara membuat Redirecting Constructor adalah dengan menambahkan : (titik dua), lalu diikuti dengan memanggil this(parameter), dimana
this() disini adalah dianggap mengakses Default Constructor.
nama Class.namaConstructor(parameter) : this(parameter);
Saat membuat Redirecting Constructor, kita tidak bisa menambahkan body pada Redirecting Constructor.
* Nah bagaimana kalau kita ingin Redirecting ke Named Constructor?
Redirecting juga bisa dilakukan ke Named Constructor
Caranya kita ganti ketika memanggil this menjadi this.namedConstructor()
caranya sangat mudah kita harus punya dulu named constructornya dulu.

*/
// Kita buat dulu class Person
class Person {
  // ↓↓↓↓↓↓↓↓↓↓ => Di bawah ini adalah fieldnya
  String? name; // ini string default nya diisi dengan "Gentha"
  String? addresses; // ini stringnya nullable
  final String country = "Indonesia"; // ini string final nya diisi dengan "Indonesia"
  int? age;

  // Constructornya ↓↓↓↓↓↓↓↓↓↓
  Person(this.name, this.addresses); // Constructor biasa
  // Named Constructor ↓↓↓↓↓↓↓↓↓↓
  Person.agenumber(this.age, String name) {
  //              ⬆️⬆️⬆️⬆️⬆️ => ini adalah contoh Initialization Parameter
  this.name = name; // <= ini adalah contoh This keyword
  }
  Person.addresses(this.addresses); // <= ini adalah contoh Named Constructor sederhana.
  Person.name(String name) {
  this.name = name;
  } //⬆️⬆️⬆️⬆️⬆️ => Contoh named constructor lagi.

  // Redirecting Constructor Dibawah ini
  //                                    ↓↓↓↓↓↓↓↓ => isi parameter ini menyesuaikan dengan parameter di Constructor, karena isinya ada 2
  Person.redirecting(String nama) : this(nama,null); // => jadi data yang dimasukannya juga 2 tetapi disini saya ingin merubah dibagian
//⬆️⬆️  Named Constru ⬆️⬆️⬆️  => Parameter baru           yang pertama, yaitu name dengan data name yang baru berupa String.
  // this di sini yaitu default constructor yaitu pada baris ke 25. 
  Person.withAddress(String address) : this(null, address); // => ini adalah contoh Redirecting Constructor.

  // Redirect ke Named Constructor
  // Disini aku mau Redirect ke named constructor yang sudah ada. yaitu pada baris ke 36.
  //                              ↓↓↓↓↓↓↓↓↓↓ => Jika ini di kasih parameter kita bisa masukan di this.addresses parameternya dengan parameternya yang ada di constructor
  Person.redirectnamedconstructor(String name) : this.addresses(name); // => name ini bisa kita ganti dengan nama yang kita inginkan.
  // Atau redirect ke Named Constructor tetapi dengan redirect constructor.
  // Disini aku mau ngambil redirecting constructornya pada baris ke 46
  //                 ↓↓ => Dibawah ini jika tidak ada parameter yang dikirimkan, maka akan mengambil default constructor. dan kita wajib mengisinya.
  Person.fromSukabumi() : this.withAddress("Sukabumi"); // => ini adalah contoh Redirecting Constructor.

  // Method Biasa.
  void sayHello(String namaOrang) {
    print("HI $name. I'm $namaOrang");
  }
  void sayHellowithAge(String namaOrang){
    print("HI $name. I'm $namaOrang, Your age is $age");
  }
}

void main(){
  var person1 = Person("Gentha", "Jl. Kebon Jeruk");
  print(person1);
  Person person2 = Person("Budi", "Jl. Perintis Kemerdekaan");
  print(person2);
  person1.sayHello("Google"); // => Pemanggilan method
  person2.sayHello("Siri");

  // Named Constructor (Pemanggilan)
  var person3 = Person.agenumber(20, "Gentha");
  person3.sayHellowithAge("Google");

  // Contoh pemanggilan Redirecting Constructor
  var person4 = Person.redirecting("Gentha");
  print(person4.name);
  print(person4.addresses);
  var person5 = Person.withAddress("Jl. Kebon Jeruk");
  print(person5.name);
  print(person5.addresses);
}
