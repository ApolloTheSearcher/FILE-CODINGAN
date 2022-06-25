// Disini kita akan membahas mengenai High Order Function.
/*
Higher-Order Function adalah function yang menggunakan function sebagai variable, parameter atau return value.
Penggunaan Higher-Order Function kadang berguna ketika kita ingin membuat function yang general dan ingin mendapatkan input yang
flexible beruba function, yang bisa dideklarasikan oleh pengguna ketika memanggil function tersebut.
Jadi singkatnya gini kita dapat mengisi sebuah fungsi parameternya itu adalah fungsi juga yang mengembalikan type data yang sama dengan
parameter fungsi yang biasa.
Contoh:
*/
// Function as Parameter (functionnya dengan menggunakan void)
//                                                   ↓↓↓↓↓↓ => Parameter disini dipengaruh oleh parameter biasa yang kita buat karena
// cuma ada satu yang String name maka Paramter didalam Function nya hanya String aja 1.
//                                                   ↓↓↓↓↓↓
void sayHello(String name, String Function(String) filteringName) {
  var filterName = filteringName(name);
  print("Hello Nama Saya $filterName");
}

// High Order Function
String FilterBadword(String name) {
  if (name == "gila") {
    return "*****";
  } else {
    return name;
  }
}

void main() {
  //                 ↓↓↓↓↓↓↓↓↓↓↓↓↓ => Ini adalah cara High Order Function digunakan. yaitu mengisi parameter pada
  sayHello("Gentha", FilterBadword); // Function dengan Function
}
