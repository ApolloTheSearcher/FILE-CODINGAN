// PEMBAHASAN SET.
/*
Hampir sama konsepnya set dengan list, tetapi pada set yang perlu diperhatikannya yaitu set tidak bisa
menampung data yang duplikat, sedangkan list bisa menampung data yang duplikat.
Kemudian perbedaan lain yang mencolok yaitu pada set tidak memperhatikan urutan data yang ada didalamnya,
sedangkan list memperhatikan urutan data yang ada didalamnya. dimana pada set itu tidak ada index.
Contoh misalkan kita akan memasukan 3 data yang bernama Eko, jika kita menggunakan list maka akan terhitung 3
data, sedangkan jika kita menggunakan set maka yang terhitung hanya 1 data Eko.
- Cara membuat set yaitu menggunakan tanda kurung kurawal {}
Set<TipeData> namaVariable = {};
var <TipeData> namaVariable = {};
final <TipeData> namaVariable = {};
*/
void main() {
  Set<int> setInt = {1, 2, 3, 4, 5};
  var setString = <String>{"1", "2", "3", "4"};
  final setDynamic = <dynamic>{1, "2", true, 10.20};
  print(setString);
  print(setInt);
  print(setDynamic);

  // Cara memanupulasi Set
  // - namaVariableSet.length => untuk menghitung jumlah data yang ada didalam set
  // - namaVariableSet.add(value) => untuk menambahkan data baru ke dalam set
  // - namaVariableSet.remove(value) => untuk menghapus data yang ada didalam set
  var setName = <String>{};
  setName.add("Eko");
  setName.add("Gentha");
  setName.remove("Gentha");
  print(setName);
  print(setName.length);

  // Selain itu kita juga jika menggunakan set kita bisa langsung mendeklarasikan set dengan data yang sudah
  // tersedia
}
