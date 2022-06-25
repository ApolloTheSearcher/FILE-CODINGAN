/*
For Looping disini kita akan membahas mengenai looping cuma menurut saya jika kalian sudah memahami Flow/jalan looping dari bahasa
pemrograman yang lain akan sama saja konsepnya seperti itu, jadi disini tidak akan terlalu mendetail karena hampir sama saja.

For looping 
syntax nya:
for(init statement;condition;post statement){
    //code (Blok perulangannya)
}
init statement akan dieksekusi hanya sekali di awal sebelum perulangan.
Kondisi akan dilakukan pengecekan dalam setiap perulangan, jika true perulangan akan dilakukan, jika false perulangan akan berhenti.
Post statement akan dieksekusi setiap kali diakhir perulangan.
Init statement, Kondisi dan Post Statement tidak wajib diisi, jika Kondisi tidak diisi, berarti kondisi selalu bernilai true. dan akan
menghasilkan yang namanya infinite looping.

While looping
hampir sama dengan for looping hanya saja lebih singkat.
while looping ini hanya ada kondisi saja, tidak ada init statement, dan post statement.
syntax nya:
while(condition){
    //code (blok perulangannya)

Do While Loop
hampir sama seperti looping dengan memiliki kondisi, dimana proses perulangan akan terjadi ketika kondisi bernilai true.
tetapi perbedaannya pada do while loop yaitu dia memiliki dimana proses yang akan di kerjakan terlebih dahulu kemudian baru akan
mengerjakan perulangannya whilenya. jadi kalau kita pakai do while loop jika pada whilenya bernilai false tetapi pada do nya terdapat
proses akan tetap di proses si do nya meskipun kondisi bernilai false.
Atau penjelasannya lebih rinci sebagai berikut:
Do While loop adalah perulangan yang mirip dengan while.
Perbedaannya hanya pada pengecekan kondisi.
Pengecekan kondisi di while loop dilakukan di awal sebelum perulangan dilakukan, sedangkan di do while loop dilakukan setelah
perulangan dilakukan.
Oleh karena itu dalam do while loop, minimal pasti sekali perulangan dilakukan walaupun kondisi tidak bernilai true.
syntax nya:
do{
    //code (blok perulangannya)
} while(condition);

- Break and Continue
Pada switch case, kita sudah mengenal kata kunci break, yaitu untuk menghentikan case dalam switch.
Sama dengan pada perulangan, break juga digunakan untuk menghentikan seluruh perulangan.
Namun berbeda dengan continue, continue digunakan untuk menghentikan perulangan saat ini, lalu melanjutkan ke perulangan selanjutnya.

- For in
For in digunakan untuk mengakses nilai dalam array. jadi ini adalah proses perulangan jika kita ingin mengakses nilai dalam array atau
kumpulan data.
Kadang kita biasa mengakses data List menggunakann perulangan.
Mengakses data List menggunakan perulangan sangat bertele-tele, kita harus membuat counter, lalu mengakses List menggunakan counter
yang kita buat.
Namun untungnya, terdapat perulangan for in, yang bisa digunakan untuk mengakses seluruh data di List secara otomatis.


*/

void main() {
  // Contoh infinite looping dengan for loop
  // for (;;) {
  //   print("Infinite looping");
  // } // Jadi jika kita menggunakan infinite looping maka jika kita membuat proses lagi di bawahnya akan terjadi dead code. karena
  // Dart sudah memberitahu bahwa infinite looping tidak akan pernah selesai atau tidak akan pernah berhenti saat kondisi false.
  // Contoh looping hanya dengan kondisi saja
  var counter = 1;
  for (; counter <= 10;) {
    print("Counter: $counter");
    counter++;
  } // Perulangan di atas akan berhenti jika data dari variable counter lebih dari 10.

  // Contoh looping dengan menggunakan init statement
  for (var angka = 0; angka <= 5;) {
    // Jika kita menggunakan cara ini jadi kita bisa langsung mendeklarasi sebuah variable di dalam looping.
    print("Angka yang diulang: $angka");
    angka++;
  }
  // Contoh looping dengan menggunakan post statement
  for (var interger = 0; interger <= 10; interger++) {
    print("Integer yang diulang: $interger");
  }

  // Contoh looping dengan menggunakan while looping.
  var jumlahBuah = 0;
  while (jumlahBuah <= 10) {
    print("Jumlah buah: $jumlahBuah");
    jumlahBuah++;
  }
  print("Buah siap di panen");

  // Contoh looping dengan menggunakan do while looping.
  var jumlahBuah2 = 0;
  do {
    print("Pertumbungan jumlah buah $jumlahBuah2");
    jumlahBuah2++;
  } while (jumlahBuah2 <= 10);
  print("Buah siap di panen");

  // Contoh looping dengan menggunakan break dan continue.
  // Menggunakan break
  var perhitungan = 0;
  while(true){
    print("Perhitungan: $perhitungan");
    perhitungan++;
    if (perhitungan > 10){
      break;
    } // Proses akan di berhentikan secara paksa jika nilai data perhitungan sudah lebih dari 10.
  }
  // Menggunakan continue
  for (var angkabulat = 0; angkabulat <= 100; angkabulat++){
    if (angkabulat % 2 == 0){
      continue;
    } // jika angkabulat modulus 2 sama dengan 0 maka proses akan di skip dan dilanjutkan ke proses selanjutnya.
    print("Angka yang ganjil kurang dari sama dengan 100: $angkabulat");
  }
  // Contoh looping tidak menggunakan for in
  print("Looping tidak menggunakan For In");
  List <String> buah = ["Apel", "Jeruk", "Mangga", "Pisang", "Pepaya"];
  for(var i = 0; i < buah.length; i++){
    int index = i + 1;
    print("Buah ke $index adalah ${buah[i]}");
  }
  // Contoh looping dengan menggunakan for in
  print("Looping dengan menggunakan For In");
  for (var i in buah){
    int index = buah.indexOf(i) + 1;
    print("Buah ke $index adalah $i");
  }
}
