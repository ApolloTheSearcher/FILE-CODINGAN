package main
import "fmt"

/*
Bayangkan berada di kelas dan mengambil bagian dalam pelajaran. Ketika kami mendengar detail penting, kami menuliskannya di buku
catatan kami untuk referensi nanti. Ide yang sama untuk menyimpan informasi penting di suatu tempat adalah alasan mengapa kami
mendeklarasikan variabel di Go. Tetapi alih-alih menuliskan informasi di buku catatan,
komputer menyisihkan sebagian ruang di memorinya untuk menyimpan nilainya. Ruang yang dialokasikan komputer disebut addreses.

Setiap alamat ditandai sebagai nilai numerik yang unik.
Setiap kita membuat sebuah variable, yang kita lakukan juga sebenarnya adalah mengambil nilai yang disimpan di alamat variable
kita dapat mengatahui alamatnya dengan menggunakan operator &.
Contoh
*/


func main(){
	fmt.Println("MEMBAHAS ADDRESES")
	// Contoh untuk melihat alamat dari variable yang kita deklarasikan
	namaGentha := "Nama saya adalah Gentha Ardaana" // ini mengisi variable langsung tanpa ditulis nama type datanya. (supaya bisa di edit)
	fmt.Println("Alamat variable dari namaGentha: ", &namaGentha) // Menampilkan alamat dari variable namaGentha

}