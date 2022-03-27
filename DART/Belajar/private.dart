class User {
  late final String nama;
  late final String password;
  late final int nis;
  // kan kalau kita biar tidak bisa diganti itu pakai constatan hanya saja kalau pakai const itu kan harus nilainya itu literal atau harus
  // diisi terlebih dahulu.
  // final itu kita gk bisa diganti karena sudah diisi sebelumnya.
  User(String nama, String password, nis) {
    this.password = "PASS : <" + password + ">";
    nama = "Nama yang anda masukan pertama:" + nama;
  }
}

void main() {
  var user = User("Rizki", "12345",099995322);
  print(user.nama);
  print(user.password);
  user.password = "231";
  print(user.password);
}
