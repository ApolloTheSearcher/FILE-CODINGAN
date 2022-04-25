package main
import "fmt"
/*
Pada pembahasan kali ini kita akan akan membahas bagaimana cara mengatasi pengubahan value dalam suatu variable pada sebuah lingkup
yang berbeda. Contoh: 
Semisalnya kita mempunyai value x pada func main yang bernilai 1 kemudian kita mempunyai value num pada func addNumber dimana didalamnya
num += 100 nah ketika kita akan mencoba memunculkan hasilnya pada func main tetapi yang ketarik adalah value x bukan pertambahan
dari num += 100 dan 1 harusnya kan 101. Unik pada bahasa golang kita belajar menganai pointers, addresses, dan deferencing untuk 
mengatasi hal seperti ini
*/
// Contoh :
func addNumberbiasa(num int) {
	num += 100 // Disini permasalahannya jika kita tidak menggunakan cara changging value
}
// Contoh mengatasinya dengan menggunakan pointers dan addresses
//                    Pointernya
//                   ↓↓↓↓↓↓↓↓↓↓↓
func addNumberSolusi(numPtr *int) {
	// numPtr Deferencing
	// ↓↓↓↓↓↓
	*numPtr += 100 // Solusinya yaitu kita harus pada fungsi ini dijadikan sebuah pointer untuk menunjukan alamat variable yang akan
	// diubah.
}

func main(){
	fmt.Println("BAB MEMBAHAS MENGENAI CARA MENGGANTI VALUE DALAM LINGKUP YANG BERBEDA (SCOPE YANG BERBEDA)")
	// Contoh Changging value in different scope yang hasilnya tidak berubah
	xBiasa := 1
	addNumberbiasa(xBiasa)
	fmt.Println(xBiasa) // Prints: 1
	// Contoh solusinya supaya nilainya bisa berubah
	// Deklarasi variablenya.
	xSolusi := 1
	//       Addressesnya yang dimasukin
	//              ↓↓↓↓↓↓↓↓
	addNumberSolusi(&xSolusi) // Ketika kita sebelumnya pada baris 16 itu sudah dijadikan sebuah pointer maka disini kita lempar dan
	// masukan alamat si variable yang akan diubah kedalam functionnya.
	fmt.Println((xSolusi)) // Prints: 101
}