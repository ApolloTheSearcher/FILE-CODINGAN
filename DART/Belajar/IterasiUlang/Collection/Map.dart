/*
Pembahasan MAP
Map adalah tipe data key-value, key itu mirip dengan index, dan value adalah datanya.
Sekilas mirip dengan list, tetapi pada list itu indexnya akan terisi otomatis jika kita menambahkan data ke dalamnya. nilainya berupa
int auto increment dimulai dari nol
Tetapi jika kita menggunakan Map, key nya bisa ditentukan dengan tipe data apapun, dan kita perlu tentukan secara manual key nya ketika
memasukkan valuenya.
Jika kita memasukan key baru dengan key yang sudah ada, secara otomatis data dengan key lama akan diganti datanya dengan yang data baru.
- Cara membuat map
Map<TipeDataKey, TipeDataValue> namaVariable = {};
var namaVariable = Map<TipeDataKey, TipeDataValue>();
var namaVariable = <TipeDataKey, TipeDataValue>{};
*/

void main(List<String> args) {
  Map<String, String> map = {
    "nama": "Eko",
    "alamat": "Jakarta",
    "umur": "20",
    "pekerjaan": "Mahasiswa"
  };
  print(map);

  // Manipulasi Map
  print(map["nama"]); // menampilkan data dengan key nama ( namaVariabelKey[key] )
  print(map["umur"]); // menampilkan data dengan key umur
  print(map.length); // menampilkan jumlah data yang ada didalam map  ( namaVariabelKey.length )
  map["nama"] = "Gentha"; // mengubah data dengan key nama menjadi Gentha ( namaVariabelKey[key] = value )
  print(map);
  print(map.keys); // menampilkan semua key yang ada didalam map ( namaVariabelKey.keys )
  print(map.values); // menampilkan semua value yang ada didalam map ( namaVariabelKey.values ) 
  print(map.isEmpty); // Ini akan menghasilkan true jika map kosong ( namaVariabelKey.isEmpty )
  print(map.isNotEmpty); // Ini akan menghasilkan true jika map tidak kosong ( namaVariabelKey.isNotEmpty )
  print(map.containsKey("nama")); // Ini akan menghasilkan true jika map memiliki key nama ( namaVariabelKey.containsKey(key) )
  print(map.containsValue("Eko")); // Ini akan menghasilkan true jika map memiliki value Eko ( namaVariabelKey.containsValue(value) )
  print(map.containsKey("alamat")); // Ini akan menghasilkan true jika map memiliki key alamat ( namaVariabelKey.containsKey(key) )
  print(map.containsValue("Jakarta")); // Ini akan menghasilkan true jika map memiliki value Jakarta ( namaVariabelKey.containsValue(value) )
  print(map.remove("umur")); // Menghapus key umur sehingga valuenya juga ikut terhapus. jadi jika kita ingi menghapus data kita remove
  // dengan keynya.
  print(map);
  map.clear(); // Menghapus semua data yang ada didalam map ( namaVariabelKey.clear() )
  print(map);

  // Mendeklarasikan Langsung Map
  // Cara mendeklarasikan sebuah data yang sudah siap dimasukan kedalam Map
  // Caranya:
  /*
  var namaVariable = {
    key1 : nama1;
    key2 : nama2;
    key3 : nama3;
  }
  */
}