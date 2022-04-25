package main

import "fmt"

/*
Bahasa golang adalah bahasa yang pass by value. dimana kita dapat melewatkan fungsi nilai dari sebuah argumen.
Dalam pengertian teknis, saat kita memanggil fungsi dengan argumen, kompiler Go secara ketat menggunakan nilai argumen
daripada argumen itu sendiri. Karena fitur ini (pass-by-value), perubahan yang terjadi di fungsi kita, tetap berada
di dalam fungsi itu.
Bayangkan seorang guru dengan kelas siswa dan guru membutuhkan siswa untuk menyelesaikan lembar kerja.
Guru akan memiliki salinan asli lembar kerja dan membuat salinan untuk ditulis oleh siswanya, tetapi siswa tidak langsung menulis
pada salinan guru. jadi si guru itu nyalin dulu.
Untuk melakukannya pada bahasa Golang, kita perlu menggunakan:
- Pointers
- Addresses
- Dereferencing
*/
/*
Sebelumnya kita membahas Addresses adalah cara dimana mengetahui alamat dari sebuah variable disimpan di memory komputer.
nah pada pembahasaan kali ini kita akan membahas mengenai Pointers. dimana Pointers adalah cara untuk melakukan menyimpan si variablenya
jadi kita bisa arahkan mau simpan variable ini ke alamat mana gitu kaya misalnya ke int atau typedata yang lainnya.
Pointer juga adalah variable yang secara khusus menyimpan alamat.
Inget ya urutan pointer adalah:
- kita harus mendeklarasikan terlebih dahulu variable
- kemudian baru sebuah Pointer akan di deklarasikan berdasarkan nilai dari alamat si variable sebelumnya
Contoh:
*/

func main() {
	fmt.Println("MEMBAHAS POINTERS")
	var PointernamaSaya *string // Jika kita menggunakan variable jangan lupa untuk menulis type datanya kemudian ditambahkan operator *
	// karena operator * itu dia akan mengarahkan keseluruhan dari fungsi si type datanya.
	namaSaya := "Nama saya adalah Gentha Ardaana" // <= ini adalah variable yang kita deklarasikan
	PointernamaSaya = &namaSaya                   // <= ini adalah pointernya yang kita deklarasikan dengan nilai dari alamat variable namaSaya
	fmt.Println("Alamat variable dari namaSaya melalui Pointer: ", PointernamaSaya)
	// Contoh lain yang tidak menggunakan variable
	namaSekolah := "SMAN 1 CIBADAK"
	PointernamaSekolah := &namaSekolah // <= ini adalah pointernya yang kita deklarasikan dengan nilai dari alamat variable namaSekolah
	// bebas ya nama untuk si Pointernya
	fmt.Println("Alamat variable dari namaSekolah melalui Pointer: ", PointernamaSekolah)

}
