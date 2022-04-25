package main
import "fmt"

/*
Sebelumnya kita membahas mengenai pointers dan addresses dimana kalau addresses itu adalah alamat yang kita simpan pada variable.
dimana menggunakan operator & untuk mengecek alamat dari variable. Kemudian Pointers adalah suatu petunjuk untuk alamat variable.
atau simplenya bahwa pointers adalah variable yang menyimpan alamat dari variable yang menggunakan operator &.
Kemudian disini kita akan membahas mengenai Deferencing dimana deferincing adalah cara lain dari Pointers yang digunakan untuk mengubah
alamat dari variable. dengan cara menggunakan operator * didepan variable Pointers dan nanti diisi oleh "Alamat yang diinginkan".
Contoh:
*/

func main(){
	fmt.Println("Bab Membahas tentang Dereferencing")
	// Contoh penggunaan Deferencing.
	// Variable yang kita deklarasikan
	lyrics := "Moments so dear" 
	// Pointers yang kita deklarasikan dengan isinya itu alamat dari si variable lyrics
	pointerForStr := &lyrics
	// Deferencing yang kita ubah alamat dari variable lyrics sebelumnya menjadi "Journeys to plan"
	*pointerForStr = "Journeys to plan" 
	fmt.Println(lyrics) // Prints: Journeys to plan
	
	// Contoh lainnya dengan menggunakan var
	// Pendeklarasian variable bertipe jenis data string
	var star string
	// Pendeklarasian Pointer untuk menyimpannya pada jenis type data string
	var starAddress *string
	// Mendeklarasikan variable star
	star = "Polaris"
	// Pointer starAddress yang menyimpan alamat dari variable star
	starAddress = &star
	// Deferencing dari isi starAddress yang sebelumnya diubah menjadi Sirius.
	*starAddress = "Sirius"
	fmt.Println("The actual value of star is", star)
}