class Siswa {
  // THIS IS FIELD ( Atribute )
  // Adalah kumpulan variable yang ada di dalam class Siswa
  static int jumlahTotal = 0;
  late String namaSiswa;
  late int semester;
  late String jurusan;
  late int rombel;
  late String alamat;
  late int nis;
  // late disini karena telat pengisiannya
  // late itu telat karena pemanggilan variable didalam constructor

  // Ini adalah constructor
  // Seolah" adalah fungsi pembuatan objek itu pertama
  Siswa(String nama, int nis, int semester, int rombel, String alamat,
      int jumlahTotal, String jurusan) {
    this.namaSiswa = nama;
    this.nis = nis;
    this.semester = semester;
    this.rombel = rombel;
    this.alamat = alamat;
    this.jurusan = jurusan;
    // digunakan untuk mememanggil variable di field
    // this diatas digunakan untuk mememanggil variable yang didefinisikan pada field
    // nama dikiri itu untuk variable yang ada di field kalau yang dikanan untuk variable yang akan di input.
    // this digunakan untuk bila ada variable yang sama
    // this digunakan untuk memanggil data yang biasa
    // kalau static yang dipanggil itu nama kelasnnya
    // contoh:
    Pohon.jumlahTotal;
    // memanggil variable static
  }
  // bisa kita memanggil variable biasa di dalam class tanpa menggunakan this
  // dan kita juga bisa memanggil variable static di dalam class tanpa menggunakan nama class nya
  // tapi ketika di luar class kita tetep menggunakan objek jika ingin mememanggil variable biasa.
  // dan kita harus tetep memanggil nama class nya jika ingin memanggil variable static
  void naiksemester() {
    semester += 1;
  }

  void pindahJurusan(String jurusan) {
    this.jurusan = jurusan;
  }

  void pindahRumah(String alamat) {
    this.alamat = alamat;
  }

  void naikKelas(int semester) {}
}

class Pohon {
  static int jumlahTotal = 0;
  // static di panggil pada void main hanya ketika memanggil jenis data / class
  // static tidak bisa di panggil oleh objek
  static void jumlahTotalPrint() {
    print("Jumlah awal sebelum ditanam adalah $jumlahTotal");
  }

  static void ubahJumlahTotal(int jumlahTotal) {
    Pohon.jumlahTotal = jumlahTotal;
    // kenapa pakai Pohon karena ini bukan field biasa tetapi static jadi harus pakai Pohon
    // pada keadaan bila nama variablenya sama.
  }

  String namaPohon;
  int jumlahDaun;
  late int panjangBatang;
  late int jumlahBuah;
  int panjangAkar;
/////////////////// DIBAWAH INI ADALAH CONSTRUCTOR ///////////////////////////////
  Pohon(this.jumlahDaun, int panjangbatang, this.panjangAkar, this.namaPohon,
      int isijumlahBuah) {
    Pohon.jumlahTotal += 1;
    this.jumlahBuah = isijumlahBuah;
    panjangBatang = panjangbatang * 3 - 1;
    // nah contoh untuk kondisi si variable jika ditambahkan late contohnya jumlahBuah.
  }
  void data() {
    print(
        "|||||||||||||||||||||| TABEL POHON $namaPohon||||||||||||||||||||||||");
    print(
        "======================= DATA POHON ==================================");
    print("Tanaman yang ditanam hari pertama yaitu $namaPohon");
    print("Hari pertama jumlah berbuahnya : $jumlahBuah buah");
    print("Panjang batang dihari pertama : $panjangBatang cm");
    print("Panjang Akar dihari pertama : $panjangAkar cm");
    print("Jumlah Daun dihari pertama ditanam : $jumlahDaun daun");
    print("Apakah berbuah: " + (jumlahBuah > 0 ? "Berbuah" : "Tidak Berbuah"));
    print(
        "=====================================================================");
  }

  static void jumlahtotaltumbuhan() {
    print("Jumlah Pohon yang di tanam : ${jumlahTotal}");
  }

  void tumbuh() {
    jumlahDaun += 1;
    this.panjangBatang += 1;
    //void berbuah() =>
    this.jumlahBuah += 1;
  }

  void gugur() => jumlahDaun -= 2;

  void apakahBerbuah() => print(jumlahBuah > 0);
  // tanda => itu untuk membuat function tanpa menggunakan return
  static String nama() {
    return "Mangga";
  }
  // contoh blok static method
  // kenapa String di atas karena digunakan untuk mereturn data returnnya
  // karena Mangga itu String maka method string nya tidak menggunakan void
  // tapi menggunakan jenis datanya yang dipakai.
}
// bisa kita memanggil variable biasa di dalam class tanpa menggunakan this
// dan kita juga bisa memanggil variable static di dalam class tanpa menggunakan nama class nya
// tapi ketika di luar class kita tetep menggunakan objek jika ingin mememanggil variable biasa.
// dan kita harus tetep memanggil nama class nya jika ingin memanggil variable static
// kita tidak boleh memanggil field biasa didalam method static
// tapi kita boleh memanggil field static didalam method biasa.

void main() {
  // Pohon.jumlahTotalPrint();
  // Pohon jeruk = Pohon(10, 10, 10, "Jeruk Florida", 0);
  // jeruk.data();
  // jeruk.gugur();
  // jeruk.tumbuh();
  // jeruk.data();
  // Pohon rambutan = Pohon(9, 21, 40, "RAMBUTAN CIBADAK INDAH", 2);
  // rambutan.data();
  // rambutan.gugur();
  // rambutan.tumbuh();
  // rambutan.data();
  // Pohon.jumlahTotalPrint();
  // rambutan.apakahBerbuah();
  // supaya tidak cape seperti ini cara menulisnya satu satu maka kita dapat menggunakan List <int>
  List<dynamic> kebunSaya = [
    Pohon(10, 10, 10, "Jeruk Florida", 0),
    Pohon(9, 21, 40, "RAMBUTAN CIBADAK INDAH", 2),
    Pohon(8, 30, 50, "PEPERONIAN", 3),
  ];
  kebunSaya.forEach((element) {
    element.data();
    element.tumbuh();
  });
  Pohon.jumlahtotaltumbuhan();
  // di atas menggunakan list supaya tidak perlu menulis banyak banyak perintah
  // tinggal menambahkan class pohon yang ingin di tambahkan
}

void main2() {
  Siswa genta = Siswa("Gentha", 1111, 3, 3, "Cibadak", 0, "Ipa");
  print(genta.namaSiswa);
  genta.namaSiswa = "Genthong";
  // digunakan untuk merubah isi dari variable nama (assigment)
  print(genta.namaSiswa);
}
