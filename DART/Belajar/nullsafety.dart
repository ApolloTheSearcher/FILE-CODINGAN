// cara mengisi supaya data null pada dart
// karena dart itu tidak bisa bahwa data itu null harus di isi
// void main() {
//   int? x;
//   print(x);
// }

class Siswa {
  late String nama;
  
  Siswa(String? nama){
    this.nama = nama ?? "Nama kosong";

  }
}
void main(){
  Siswa siswa = Siswa(null);
  print(siswa.nama);
}