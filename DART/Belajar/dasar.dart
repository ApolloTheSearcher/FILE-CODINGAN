void generateFibonacci(int n) {
  List<int> fib = [0, 1];
  for (int i = 2; i < 10; i++) {
    fib.add(fib[i] + fib[i++]);
  }
  print(fib);
}

void main() {
  int n = 10;
  generateFibonacci(n);
}

var angka = 10;//var itu langsung jenis datanya diisi
// dynamic itu any untuk apa saja
