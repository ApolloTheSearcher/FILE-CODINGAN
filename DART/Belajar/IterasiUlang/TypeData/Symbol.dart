// pada bahasa dart ada yang namanya itu symbol, meskipun jarang digunakan symbol ini.
// Pada symbol bisa kita gunakan sebagai constant
/*
Untuk membuat Symbol, Kita bisa mengggunakan tanda #, Tetapi jika kita ingin membuat Symbol dengan nama yang
mengandung spasi maka kita bisa menggunakan Symbol("text") 
Contoh:
*/
void main(List<String> args) {
  Symbol symbolNama = Symbol("Gentha ARDAANA");
  var symbolNama2 = #GenthaArdaana; // Jika kita menggunakan tanda # tidak boleh ada spasi.
  print(symbolNama);
  print(symbolNama2);
}
