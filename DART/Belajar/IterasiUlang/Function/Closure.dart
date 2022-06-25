/*
Closure adalah kemampuan sebuah function atau anonymous function berinteraksi dengan data-data disekitarnya dalam scope yang sama
Harap gunakan fitur closure ini dengan bijak saat kita membuat aplikasi
*/
// Contoh Closure
void main() {
  var counter = 0;
  void increment() {
    print("Increment");
    counter++;
  }
  print(counter);
  increment();
  increment();
  print(
      counter); // Ini nilai nya akan menjadi 2 karena kita menggunakan closure kenapa bisa begitu , kita dapat lihat pada
  // Function increment karena fungsi increment ini masih satu scope dengan variable counter jadi didalam function increment kita dapat
  // mengakses variable counter yang berada di dalam scope main. sehingga terjadi proses decrement pada counter. dan menjadi nilainya 2
  // karena kita memanggil function increment 2 kali.
}
