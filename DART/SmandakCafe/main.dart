import 'menu.dart';
//import 'food.dart';
//import 'drink.dart';

void main(List<String> args) {
  Menu.clear();
  int uang = 300000;
  print(Menu.namaKelas);
  Menu.welcome();
  Menu.separator();
  Menu.namaMenu();
  Menu.Head();
  Menu.tampilanMenu();

  // looping dibagian ini untuk cara supaya bisa milih menu lagi
  while (true) {
    Menu.separator();
    // print(Menu.menus[2].nama);
    // print(Menu.menus[2].stock);
    // print(Menu.formatUang(Menu.menus[2].harga));
    // cara memanggil method biasa itu tidak memakai nama classnya tapi nama variablenya
    // cara memanggil method static itu memakai nama classnya.
    //print(Menu.formatUang(50000000));
    print(
        "Pilihan pesanan [1 - ${Menu.menus.length}] [q - keluar(selesai membeli)] [m - lihat menu] ");
    String cek = Menu.input("Pilih");
    if (cek == "q")
      break;
    else if (cek == "m") {
      Menu.clear();
      print("Sisa Uang Kamu: ${Menu.formatUang(uang)}");
      Menu.separator();
      Menu.namaMenu();
      Menu.Head();
      Menu.tampilanMenu();
      continue;
    }

    int pilihan = int.parse(cek);

    if (pilihan > 0 && pilihan <= Menu.menus.length) {
      // digunakan untuk mengecek apakah nomor menu ada di table menu
      Menu.clear();
      Menu terpilihan = Menu.menus[pilihan - 1];
      print(">> " + terpilihan.printItem());
      Menu.separator();
      int jumlah = int.parse(Menu.input("Jumlah pesanan "));
      print(">> $jumlah porsi");
      int subtotal = terpilihan.harga * jumlah;

      if (subtotal <= uang) {
        if (terpilihan.beli(jumlah)) {
          print(
              "Kamu membeli ${terpilihan.nama} seharga ${Menu.formatUang(subtotal)}");
          uang -= subtotal;
        } else {
          print("Maaf Stock Habis :(");
        }
      } else {
        print("Maaf uangmu tidak cukup");
      }
      if (uang > 0) {
        print("Sisa uang : " + Menu.formatUang(uang));
      } else {
        print("Uangmu habis!!!");
      }
    } else {
      print("Maaf menu tidak tersedia");
    }
  }

  Menu.clear();
  Menu.inVoice();
  Menu.separator();
  Menu.cetakBonBeli();
  Menu.separator();
  Menu.goodbye();
}
