import 'dart:io' as io; // digunakan untuk input

class Menu {
  // Kelas
  static const String namaKelas =
      "===== Menu Smandak Cafe (Logo Smandak) ======";
  // static  String get menu => " ";
  // diatas ini adalah static method jadi method bukan field

  // Map untuk bikin struk bonBeli
  static final Map<Menu, int> bonBeli = {};

  // Static Method Invoice
  static inVoice(){
    print("\t=====Demikian struk pembelian anda=====");
  }

  // Static Method welcome
  static welcome() {
    print(
        "Selamat datang di Smandak Cafe\n\tSelamat Memesan\nPelanggan senang kamipun nyaman ");
  }

  // Static Method GOODBYE
  static goodbye() {
    print(
        "Terimakasih telah mengunjungi Smandak Cafe\n\t== Jangan bosan-bosan ya :) ==");
  }

  // Static Separator
  static separator() {
    print("==========================================================");
  }

  // Static Header
  static Head() {
    print("No" + "\tNama" + "\t\t\t" + "Harga" + "\t\t" "Stock");
  }

  // Static Nama Menu
  static namaMenu() {
    print("\t\t MENU DARI SMANDAK CAFE");
  }

  // Static Method
  static final List<Menu> menus = [
    Menu("Nasi Goreng", 15000, 15),
    Menu("Seblak", 12000, 20),
    Menu("Cilok isi 12", 12000, 25),
    Menu("Es Teh", 3000, 30),
    Menu("Boba Coklat", 10000, 40),
    Menu("Boba Strawberry", 10000, 50)
  ];

  // Static method
  static String formatUang(int nilaiUang) {
    String after = "";
    String before = nilaiUang.toString();
    for (int i = 0; i < before.length; i++) {
      // .lenght itu digunakan untuk menghitung jumlah karakter dalam string seperti len di python.
      after += before[i];
      if ((i + 1) % 3 == (before.length % 3) && (i + 1) != before.length) {
        after += ".";
      }
    }
    return "Rp." + after + ",-";
  }

  // Static method cls
  static void clear() {
    print(io.Process.runSync("cls", [], runInShell: true).stdout);
    io.stdout.write("\x1B[2J\x1B[0;0H");
  }

  // Static method Tampilan
  static void tampilanMenu() {
    for (int i = 0; i < Menu.menus.length; i++) {
      print("${i + 1}. ${Menu.menus[i].printItem()}");
    }
  }

  // Static method Input
  static String input([String? pesan]) {
    if (pesan != null) io.stdout.write(pesan + " : ");
    return io.stdin.readLineSync() ?? "";
  }

  // static Final BONBELI
  // sebelum kita membuat struk bonBelinya kita harus mebuat map nya
  static void cetakBonBeli() {
    print("No." + "\tNama" + "\t\t\t" + "Harga" + "\t\t" "Stock");
    int index = 1;
    Menu.bonBeli.forEach((key, jumlahBeli) {
      print("$index \t${key.printItemBon()} \t$jumlahBeli");
      index++;
    });
  }

  // FIELD
  String nama;
  int harga;
  int stock;

  // Constructor
  Menu(this.nama, this.harga, this.stock);
  // Method beli
  bool beli(int jumlah) {
    if (stock >= jumlah) {
      stock -= jumlah;
      if (bonBeli[this] == null) {
        bonBeli[this] = jumlah;
      } else {
        bonBeli[this] = bonBeli[this]! + jumlah;
      }
      return true;
    } else {
      return false;
    }
  }

  // Method printitem
  String printItem() {
    // print("Nama : $nama");
    // print("Harga : ${Menu.formatUang(harga)}");
    // print("Stock : $stock");
    String tab = "\t";
    String tab2 = "\t";
    if (nama.length <= 14) {
      tab += "\t\t";
    } else {
      tab += "\t";
    }
    return (nama + tab + Menu.formatUang(harga) + tab2 + stock.toString());
  }

  // Method printitem untuk struk bonBeli
  String printItemBon() {
    String tab = "\t";
    if (nama.length <= 9) {
      tab += "\t\t";
    } else {
      tab += "\t";
    }
    return (nama + tab + Menu.formatUang(harga));
  }
}
