// Hampir sama cara penulisan function pada bahasa golang seperti dart karena memang 2 bahas itu jenisnya sama
// yaitu midlelanguage.
package main
import(
	"fmt"
	"time"
	"math"
)

func fungsiNamaSaya(){
	fmt.Println("Nama saya adalah Gentha Ardaana")
}

func performAddition() {
	x := 5
	y := 7
	fmt.Println("The sum of", x, "and", y, "is", x + y)
}
//           String di bawah ini digunakan untuk nanti yang di return itu akan menjadi nilai typenya string
// 						⬇️⬇️
func isLateInNewYork() string{
	var lateMessage string
	t := time.Now()
	tz, _ := time.LoadLocation("America/New_York")
	nyHour := t.In(tz).Hour()
	if nyHour < 5 {
		lateMessage = "Goodness it is late"
	} else if nyHour < 16 {
		lateMessage = "It's not late at all!"
	} else if nyHour < 19 {
		lateMessage = "I guess it's getting kind of late"
	} else {
		lateMessage = "It's late"
	}
	
	// Return the string lateMessage
	return lateMessage // nilai yang akan dikembalikan adalah berupa string

}

// Disini contoh fungsi di bahasa golang dengan function parameter dan return.
func namaSaya(nama string) string{
	fmt.Printf("Nama saya adalah %s\n", nama)
	return nama // kita return si parameternya supaya bisa di panggil di fungsi main
	// tetapi jika proses sudah di deklarasikan kita ganti returnnya dengan variable yang menyimpan data prosesnya.
}

// Contoh pembuatan fungsi dengan mengembalika nilainya menjadi sebuah desimal float
//   tanda di bawah ini maksudnya nanti nilai hasil yang akan dikembalikan/return adalah sebuah desimal float
//   							   ↓↓↓↓↓↓↓
func specialComputation(x float64) float64{
	return math.Log2(math.Sqrt(math.Tan(x)))
}

// Disini kita akan membahas mengenai cara lain untuk mengembalikan nilai return karena sebelumnya bahwa mengembalikan nilai hanya
// satu jenis data, namun tidak sampai situ bahwa golang ini bisa multiple return function loh. dimana nilai yang ingin dikembalikan
// bisa lebih dari satu.
// Langsung kita eksekusi
// Contoh:
// Yang di tandai ini dia mengembalikan nilai dengan 2 type data yaitu string dan float32 kenapa bisa gitu?
// karena didalam fungsinya itu terutama yang akan di return kan kalau dibawah sini itu gradeLetter dan averageGrade mereka berdua
// Berjenis type data string dan float32 jadi kita returnnya juga harus menggunakan 2 type data yang sama.
// 													↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
func GPA(midtermGrade float32, finalGrade float32) (string, float32) {
	averageGrade := (midtermGrade + finalGrade) / 2
	var gradeLetter string
	if averageGrade > 90 {
		gradeLetter = "A - SELAMAT ANDA MENDAPATKAN NILAI A DAN PERTAHANKAN ATAU TINGKATKAN KEMBALI"
	} else if averageGrade > 80 {
		gradeLetter = "B - SELAMAT ANDA MENDAPATKAN NILAI B DAN TINGKATKAN KEMBALI"
	} else if averageGrade > 70 {
		gradeLetter = "C - SELAMAT ANDA MENDAPATKAN NILAI C DAN TINGKATKAN KEMBALI"
	} else if averageGrade > 60 {
		gradeLetter = "D - SELAMAT ANDA MENDAPATKAN NILAI D DAN TINGKATKAN KEMBALI"
	} else {
		gradeLetter = "F - HARAP MENGULANG SEMESTER DI TAHUN DEPAN!"
	}
	return gradeLetter, averageGrade 
}

// Setelah kita diketahui cara mengembalikan/return nilai dari suatu fungsi dengan lebih dari 1 type data
// Kemudian kita akan membahas mengenai bagaimana kita menunda suatu suatu nilai di dalam fungsi
// Nah ternyata pada golang terdapat fungsi yang dapat mengatasi hal itu dengan menggunakan keyword defer
// defer biasanya digunakan untuk loggin, penulisan file, dan utilitas lainnya
// Contoh:
func queryDatabase(query string) string {
	var result string
	connectDatabase() // Jika fungsi ini kita tambahkan defer maka nanti fungsi ini akan di eksekusi terakhir.
	// Add deferred call to disconnectDatabase() here
	defer disconnectDatabase() // Fungsi deffer jadi nanti fungsi dari disconnectDatabase akan di eksekusi diakhir / muncul di akhir
	// Nah pada defer ini dia urutannya itu apabila terdapat fungsi defer lain tetapi urutannya lebih dahulu maka fungsi itu yang akan
	// di eksekusi terakhir dari pada defer setelah fungsi yang di defer yang pertama
	if query == "SELECT * FROM coolTable;" {
		result = "NAME|DOB\nVincent Van Gogh|March 30, 1853"
	}  
	fmt.Println(result)
	return result
} // Fungsi di bawah ini digunakan untuk connectDatabase dan disconnectDatabase
func connectDatabase() {
	fmt.Println("Connecting to the database.")
}
func disconnectDatabase() {
	fmt.Println("Disconnecting from the database.")
}


func main(){ // <= function main ini digunakan untuk mengumpulkan semua fungsi yang dibuat kemudian di proses
	// melalui compiler
	fungsiNamaSaya()
	fmt.Println("DI ATAS INI ADALAH CONTOH FUNGSI")

	// Kemudian Lingkup (scope dari bahasa golang ini) tidak bisa di panggil apa bila variable nya tidak dalam 
	// scope dari function yang sama.
	// Contoh:
		performAddition()
		fmt.Println("What if", /* x */ "was different?") // ERROR: x is not defined karena x bukan lingkup func main.


	// Disini kita akan membahas caranya melakukan pengembalian pada fungsi yaitu dengan menggunakan return
	// cara penulisannya adalah sebagai berikut:
	/* 
	func namaFungsi() typeData{
		var nilaiReturn typeData
		// Code
		// return nilaiReturn
	}
	*/
	// Contoh:
	// Kita akan mengambil nilai fungsi isLateInNewYork() dan kita akan menampilkan hasilnya
	var myLate string
	myLate = isLateInNewYork()
	fmt.Println(myLate)

	// Disini kita akan memanggil fungsi namaSaya() dan kita akan menampilkan hasilnya
	namaAku := "Gentha Ardaana"
	namaSaya(namaAku) // nilai yang akan dikembalikan adalah berupa string
	// Outputnya adalah: Nama saya adalah Gentha Ardaana

	// Disini kita akan memanggil fungsi specialComputation() dan kita akan menampilkan hasilnya 
	// Fungsi ini digunakan untuk menghitung nilai komputasi aneh
	var a, b, c, d float64 // <= mendeklarasi nilai var(variable) a,b,c,d dengan type data float64
	a = .0214
	b = 1.02
	c = 0.312
	d = 4.001
	// Memanggil fungsinya 
	a = specialComputation(a)
	b = specialComputation(b)
	c = specialComputation(c)
	d = specialComputation(d)
	// Menampilkan hasilnya
	fmt.Println(a, b, c, d)

	// Disini kita akan memanggil fungsi GPA() dan kita akan menampilkan hasilnya pada baris ke-64
	var myMidterm, myFinal float32
	myMidterm = 89.4
	myFinal = 74.9
	var myAverage float32
	var myGrade string
	myGrade, myAverage = GPA(myMidterm, myFinal)
	fmt.Println(myAverage, myGrade)
	// Outputnya adalah: 82.12 - SELAMAT ANDA MENDAPATKAN NILAI B DAN TINGKATKAN KEMBALI

}