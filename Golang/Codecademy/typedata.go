package main
import "fmt"

func main(){
	var a string
	var b int8 // Jika variable kita membuat variable tetapi belum di pakai di akan error saat compilenya
	var c bool // bacaan nya yaitu variable_name declared but not
	const Nama = "Ini adalah contoh konstanta"
	a = "Gentha Ardaana"
	b = 10
	c = true
	fmt.Println("Cara penulisannya adalah : ", Nama)
	fmt.Println("Nama saya" + a)
	fmt.Println("Nilai saya", b)
	fmt.Println("Nilai saya", c)
}


/*
ternyata dibahasa golang type data tidak jauh sama
hanya saja ada bahasa golang type datanya di awali dengan var
dan jenis type data yang bisa digunakan adalah:
string = kalimat
int8 = integer untuk bilangan bulatnya pake 8
bool = boolean
float = desimal	
*/