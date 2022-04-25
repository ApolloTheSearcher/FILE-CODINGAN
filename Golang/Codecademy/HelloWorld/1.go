package main
import "fmt"
import t "time" // => t itu artinya untuk menginisial supaya bisa menggunakan fungsi pada module time
// membuat hewan dengan print wkwk
func main(){
	fmt.Println("  __      _")
	fmt.Println("o'')}____//")
	fmt.Println(" `_/      )")
	fmt.Println(" (_(_/-(_/ ")
	fmt.Println((t.Hour.Nanoseconds()))
	t.Now()
}
/*
func main() {
	fmt.Println("Hello, World")
	fmt.Println("aku cinta kamu") 
	fmt.Println(t.Now()) // => maka akan menampilkan waktu saat ini

}
*/

/*
ternyata di dalam bahasa go itu pembacaan programnya dari atas ke bawah, jadi kalau misalkan kita kita print 2 string
dia tidak akan menyambung
kemudian kita juga dapat import lebih dari 1 module kemudian bisa diberi inisial si modulenya

karena golang ini masih bahasa pemrograman yang baru dikembangkan oleh google sehingga jika terdapat error atau syntax error
bisa langsung di cari di google untuk mengatasinya
seperti forum forum online:
stack OverFlow
situs resmi bahas Go
Bahasa go juga memiliki sistem dokumentasinya sendiri (untuk mengetahui informasi lebih lanjut tentang bahasa go)
cara menggunakannya:
gunakan perintah (go doc <nama module atau package><fungsi module atau packagenya>) digunakan di terminal atau console

*/