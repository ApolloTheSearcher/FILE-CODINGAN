/*
  Pembahasan mengenai null
  null adalah sebuah nilai yang kosong atau tidak ada nilai. BUKAN NOL(0) YA TAPI KOSONG!.
  Secara default jika kita membuat sebuah variable, maka data harus diisi, jika tidak diisi maka variable tidak
  bisa digunakan.
  Namun jika masih ingin ngeh membuat variable dengan mengisi datanya kosong/null kita dapat menggunakan operator
  tanda tanya (?). Seperti:
  TipeData? namaVariable = null;
*/

void main(List<String> args) {
  // int nilai = null => error
  // print(nilai);
  // Pada nilai akan error karena tidak ada tanda tanya (?).
  int? nilai2 = null;
  print(nilai2);

  String? nama;
  nama = null;
  print(nama);
}
