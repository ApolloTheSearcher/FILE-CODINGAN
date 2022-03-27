// var a = 10; // jadi var bisa di deklarasi ulang

// console.log(a);

// var a = "Hello World";
// console.log(a);

// let b = 10; // jadi untuk let tidak bisa di deklarasi ulang si letnya
// // kalau variablenya bisa diganti tanpa menulis let lagi
// b = "Ini let b";

// console.log(b);

let input = 10;
for (let i = 1; i <= input; i++) {
    if (input % i == 0 &&  i != 5) {
        console.log(i);
    }
}