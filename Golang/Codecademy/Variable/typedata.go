package main

import (
	"fmt"
)

func main(){
	var a string
	var b int8 // Jika variable kita membuat variable tetapi belum di pakai di akan error saat compilenya
	var c bool // bacaan nya yaitu variable_name declared but not
	const NAMA = "Ini adalah contoh konstanta"
	a = "Gentha Ardaana"
	b = 10
	c = true
	// Selain itu kita juga dapat mendeklarasikan variable langsung dengan tipe datanya contoh:
	var iniAngkaGanjil float32 = 8.0

	fmt.Println("Cara penulisannya adalah : ", NAMA) //Penggabungan variable disebut concatenation
	fmt.Println("Nama saya" + a) 
	fmt.Println("Nilai saya", b)
	fmt.Println("Nilai saya", c)
	fmt.Println("Nilai saya", iniAngkaGanjil)
	// Jika kita membuat sebuah variable dan mendeklarasikan tetapi kita tidak memberi nilainya maka nilainya
	// ketika kita ingin ngeprint nya maka hasilnya akan Nol jika type datanya berupa nilai
	// jika type datanya bersifat string maka akan menghasilkan "Doesn't print anything"
	// jika type datanya boolean akan menghasilkan false
	// Contoh :
	var iniAngkaNol int8
	var stringKosong string
	var booleanKosong bool
	fmt.Println("Nilai saya", iniAngkaNol)
	fmt.Println(stringKosong)
	fmt.Println(booleanKosong)


}


/*
ternyata dibahasa golang type data tidak jauh sama
hanya saja ada bahasa golang type datanya di awali dengan var
dan jenis type data yang bisa digunakan adalah:
string = kalimat
int8 = integer untuk bilangan bulatnya pake 8 dan hanya menyimpan 8bits dari bilangan bulat
bool = boolean
float = desimal	
*/