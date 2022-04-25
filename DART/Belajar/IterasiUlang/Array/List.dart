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
  */
  // Create list of interger
  List<int> listInt = [1, 2, 3, 4, 5];
  // Create list of String
  var listString = <String>["1", "2", "3", "4"];
  final listDynamic = <dynamic>[1, "2", true, 10.20];
  print(listString);
  print(listInt);
  print(listDynamic);
}
