class Animal {
  //=> penulisan class itu menggunakan CamelCase
  // atribute
  String kategori;
  String? nama;
  int? weigth; // kg
  // Untuk Mengisi data atribute (constrator)//
  // Positional Arguments
  // contoh
  // Animal(this.kategori, this.nama, this.weigth);
  // named argument
  // contoh:
  Animal({required this.kategori, this.nama, this.weigth});
  // Method
  // contoh Method(fungsi)
  makan(int beratBadan) {
    weigth = weigth! + beratBadan;
    // nah kenapa error karena kita disini pada variable weight di atribute itu kan tipe datanya null karena pake fitur null safetv
    // jadi weight di situ dibaca tidak ada datanya karena null safety
    // kita bisa mengatasinya dengan menambahkan penegasan yaitu menggunakan tanda (!)
    // pada weigth di method itu kita menggunakan tanda (!)
  }
}

void main() {
  /*
  Animal hewan1 = Animal(kategori: "Reptil", nama: "Komodo", weigth: 20);
  print("Kategorinya adalah ${hewan1.kategori}");
  print("Nama Hewan adalah ${hewan1.nama}");
  print("Berat Hewan adalah ${hewan1.weigth} Kg");
  */
  // kita bisa menggunakan yang namanya cascade notation untuk mengganti data
  // misalnya mau ganti nama hewannya
  Animal hewan1 = Animal(kategori: "Reptil", weigth: 20)
    ..nama = "Anjing"
    ..weigth = 1000;
    // diatas disebutnya casecade notation

  print("Kategorinya adalah ${hewan1.kategori}");
  print("Nama Hewan adalah ${hewan1.nama}");
  print("Berat Hewan adalah ${hewan1.weigth} Kg");
  // selain itu kita dapat merubah namanya ketika di tengah jalan misalnya ceritanya setelah makan hewan langsung berubah
  hewan1.makan(10);
  // contoh mengubah nama atau yang lain bisa langsung dengan variable datanya di ganti
  hewan1.nama = "KANGGURU";
  hewan1.kategori = "Mamalia";
}
