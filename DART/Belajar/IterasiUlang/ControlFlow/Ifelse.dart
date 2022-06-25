/*
Pembahasan If else
If itu adalah percabangan jika bernilai True diakan akan dieksekusi sedangkan else adalah jika nilai if 
tidak true maka else akan di eksekusi.
Contoh:
*/
/*
ELSE IF
else if ini adalah bisa kita sebut sebagai kondisi dimana jika pada if tidak terpenuhi terdapat kondisi lain 
yaitu else if, nah kenapa kita tidak menggunakan if aja, jika kita menggunakan if aja maka jika terdapat 2 kondisi
yang bernilai true maka dua duanya akan tereksekusi sedangkan jika menggunakan elseif maka jika sudah 1 kondisi true
maka seterusnya tidak akan di eksekusi.
*/
void main(List<String> args) {
  var nilaiBudiMTK = 90;
  var nilaiKKMMTK = 85;
  if (nilaiBudiMTK > nilaiKKMMTK) {
    print("Budi kamu lolos mata pelajaran saya");
  } else if (nilaiBudiMTK == nilaiKKMMTK) {
    print("Nilai kamu pas-pas an budi ditingkatkan kembali");
  } else {
    // Kondisi else terproses jika kondisinya bernilai false.
    print("Kamu tidak lolos mata pelajaran saya");
  }
}
