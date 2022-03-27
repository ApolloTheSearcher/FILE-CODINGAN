// class itu ada yang namanya 2 atribut
// yaitu atribute(properties) dan Behavior(method)
// atribute => variable
// Behavior => Funcition
// contoh class:
class Animal {
  //=> penulisan class itu menggunakan CamelCase
  // atribute
  String kategori;
  String? nama;
  int? weigth; // kg
  // Untuk Mengisi data atribute (constrator)
  // Animal(this.kategori, this.nama, this.weigth);
  // di atas adalah positional argument
  // => namanya bebas karena itu buat penamaan
  // => bagian kanan setelah = itu artinya dia akan mengambil data yang nanti kita input setelah itu di proses dan di lempar ke atribute
  // penggunaan this itu untuk membedakan variable yang ada di atribute atau yang ada di constarctor
  // tidak ingin menulis this di sini kita bisa langsung tembak saja thisnya didalam constrator untuk mempersingkatnya
  // untuk mengisi field dibawah kita menggunakan
  // di atas adalah contoh constrator yang singkat. (jika tidak ada proses yang dibutuhkan maka kita bisa langsung menulis constrator tanpa membuat proses)
  // Jika ada proses bisa menggunakan constrator dibawah ini
  // selain positional argument kita bisa menggunakan named argument
  // named argument => nama variabel yang kita buat
  // contoh:
  Animal({required this.kategori, this.nama,this.weigth});
  // jika terjadi error kita bisa menggunakan required karena itu disebabkan karena adanya nul Savety
  // atau menambahkan tanda ? pada jenis data pada argument jika tidak ingin menggunakan required
  // ketika kita menggunakan required bisa kita hapus late di argument atau tidak juga bisa
}

void main() {
  //contoh cara pemanggilan
  // dibawah cara pemanggilan ketika menggunakan positional argument
  // Animal hewan1 = Animal("Reptil", "Komodo", 20);
  // jika kita menggunakan named argument cara pemanggilannya kita tulis si nama variablenya kemudia datanya
  // jika kita menggunakan named argument posisinya bisa tidak sesuai urutan
  Animal hewan2 = Animal(weigth: 30, nama: "Biawak", kategori: "Reptil");
  Animal hewan1 = Animal(kategori: "Reptil", nama: "Komodo", weigth: 20); 
  print("Kategorinya adalah ${hewan1.kategori}");
  print("Nama Hewan adalah ${hewan1.nama}");
  print("Berat Hewan adalah ${hewan1.weigth} Kg");
  print("-------------------------------------");
  print("Kategorinya adalah ${hewan2.kategori}");
  print("Nama Hewan adalah ${hewan2.nama}");
  print("Berat Hewan adalah ${hewan2.weigth} Kg");
}
