// List adalah sebuah kumpulan data.
// Setiap kita membuat list kita harus mengisinya
// List menggunakan tanda [] => kurung siku
// semua typedata memiliki object tetapi list sendiri memiliki property, method dan operator.
void main(List<String> args) {
  // Cara membuat list kita dapat menggunakan type datanya atau bisa menggunakan var atau final
  /*
  - Membuat list dengan type datanya di awal:
  List<tipeData> namaVariable = [];
  - Membuat list dengan var atau final:
  var namaVariable = <TipeData>[];
  final namaVariable = <TipeData>[];
  NOTE : JIKA KITA TIDAK MENAMBAHKAN TIPE DATANYA MAKA OTOMATIS LISTNYA AKAN BERUPA DYNAMIC
  */
  // Create list of interger
  List<int> listInt = [1, 2, 3, 4, 5];
  // Create list of String
  var listString = <String>["1", "2", "3", "4"];
  final listDynamic = <dynamic>[1, "2", true, 10.20];
  print(listString);
  print(listInt);
  print(listDynamic);

  // Menambahkan Data ke List
  // Bayangkan list adalah sebuah tabel nah kita dapat menambahkan isinya didalamnya
  // Ukuran list akan otomatis bertambah ketika kita menambahkan data kedalam list
  // Cara menambahkan data kedalam sebuah list kita dapat menggunakan method add(value)
  // Dan untuk mengetahui berapa jumlah data yang ada didalam list kita dapat menggunakan property length
  // Contoh:
  List<String> listNama = []; // Karena disini type datanya adalah string maka kita hanya bisa menambahkan data bertype string.
  listNama.add("Rizki"); // Kita dapat menggunakan method add untuk menambahkan sebuah data ke dalam list
  listNama.add("Gentha"); // tetapi jika kita ingin menambahkan kumpulan data ke dalam sebuah list kita dapat menggunakan method
  listNama.add("Gibran"); // addAll.
  listNama.addAll(["Budi", "Bambang", "Joko"]); // => Method addAll untuk menambahkan kumpulan data ke dalam sebuah list
  print(listNama);
  print(listNama.length); // => Method length untuk mengetahui berapa jumlah data yang ada didalam list

  // Index
  /*
  Saat kita menambahkan data kedalam list, secara otomatis data tersebut memiliki index bertype int, index ini digunakan untuk kita 
  mengakses, mengubah, atau menghapus data yang ada didalam list.
  Index dimulai dari 0 dan kemudian akan terus bertambah seiring dengan kita menambahkan data.
  cara menghitung index adalah (panjang data - 1).
  Contoh:
  */
  // Manipulasi data di List
  /*
  Operator/Methodnya:
  - list.add(value) => untuk menambahkan data ke dalam list
  - list[index] => untuk mengambil data di list
  - list[index] = value => untuk mengubah data di list
  - list.removeAt(value) => untuk menghapus data di list, index akan secara otomatis bergeser.
  Contoh:
  */
  print(listNama[0]); // => Menampilkan data pada index ke 0
  listNama[1] = "Hartanto"; // => Mengubah data pada index ke 1
  listNama.removeAt(2); // => Menghapus data pada index ke 2, kemudian bergeser yang tidak terpakai.
  print(listNama);

  // Mendeklarasikan list secara langsung
  /*
  Kita dapat langsung loh mendeklarasikan langsung data ke dalam list jika memang datanya sudah ada atau siap
  caranya:
  List<TipeData> namaVariable = [data1, data2, data3, ..., dataN];
  var namaVariable = [
    data1, 
    data2,
    data3, 
    ..., 
    dataN
];
  final namaVariable = [
    data1, 
    data2,
    data3, 
    ..., 
    dataN
];
  var namaVariable = <tipeData>[data1, data2, data3, ..., dataN];
  */

}
