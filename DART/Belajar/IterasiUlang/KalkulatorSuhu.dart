import "dart:io";

void main() {
  print("----- Selamat datang pada Aplikasi Konversi Suhu -----");
  print("Suhu yang tersedia:\n1. Celcius\n2. Reamur\n3. Kelvin\n4. Fahrenheit");
    stdout.write("Konversi Suhu apa yang anda inginkan : \n");
    var f = stdin.readLineSync()!;
    if (f == "Celcius" || f == "celcius" || f == 1) {
      stdout.write("Masukkan suhu dalam Celcius : \n");
      var celcius = double.parse(stdin.readLineSync()!);
      var reamur = celcius * 4 / 5;
      var kelvin = celcius + 273.15;
      var fahrenheit = celcius * 9 / 5 + 32;
      print("Suhu dalam Celcius : $celcius");
      print("Suhu dalam Reamur : $reamur");
      print("Suhu dalam Kelvin : $kelvin");
      print("Suhu dalam Fahrenheit : $fahrenheit");
    } else if (f == "Reamur" || f == "reamur" || f == 2) {
      stdout.write("Masukkan suhu dalam Reamur : \n");
      var reamur = double.parse(stdin.readLineSync()!);
      var celcius = reamur * 5 / 4;
      var kelvin = reamur * 5 / 4 + 273.15;
      var fahrenheit = reamur * 9 / 4 + 32;
      print("Suhu dalam Celcius : $celcius");
      print("Suhu dalam Reamur : $reamur");
      print("Suhu dalam Kelvin : $kelvin");
      print("Suhu dalam Fahrenheit : $fahrenheit");
    } else if (f == "Kelvin" || f == "kelvin" || f == 3) {
      stdout.write("Masukkan suhu dalam Kelvin : \n");
      var kelvin = double.parse(stdin.readLineSync()!);
      var celcius = kelvin - 273.15;
      var reamur = kelvin * 4 / 5;
      var fahrenheit = kelvin * 9 / 5 - 459.67;
      print("Suhu dalam Celcius : $celcius");
      print("Suhu dalam Reamur : $reamur");
      print("Suhu dalam Kelvin : $kelvin");
      print("Suhu dalam Fahrenheit : $fahrenheit");
    } else if (f == "Fahrenheit" || f == "fahrenheit" || f == 4) {
      stdout.write("Masukkan suhu dalam Fahrenheit : \n");
      var fahrenheit = double.parse(stdin.readLineSync()!);
      var celcius = (fahrenheit - 32) * 5 / 9;
      var reamur = (fahrenheit - 32) * 4 / 9;
      var kelvin = (fahrenheit + 459.67) * 5 / 9;
      print("Suhu dalam Celcius : $celcius");
      print("Suhu dalam Reamur : $reamur");
      print("Suhu dalam Kelvin : $kelvin");
      print("Suhu dalam Fahrenheit : $fahrenheit");
    } else {
      print("Maaf, $f tidak tersedia pada aplikasi ini");
    }
    print("----- Terima Kasih telah menggunakan Aplikasi Konversi Suhu -----");
}
