// Pada bab ini kita akan membahas mengenai conditionals yang nanti akan membahas terkait branching seperti
// If, Else If, Else, dan Switch.
package main
import(
	"fmt"
	"math/rand"
	"time"
)

func main() {
	nilaiBoolean := true
	if nilaiBoolean {
		fmt.Println("Nilai boolean adalah true")
	
	} else if nilaiBoolean == false { // else if bisa digunakan untuk menambahkan kondisi lain
		fmt.Println("Nilai boolean adalah false")

	}else { // Jika nilaiBoolean bernilai false dia akan mencetak "Nilai boolean adalah false"
		fmt.Println("Nilai boolean adalah false")
	}

	// Logical Operator
	// Operator yang digunakan untuk mendapatkan nilai berupa boolean (true/false)
	// operatornya yaitu && (AND), || (OR), ! (NOT)
	// Contoh:
	rightTime := true
	rightPlace := true

	// Menggunakan operator &&
	if rightTime && rightPlace {
		fmt.Println("We're outta here!")
	} else {
		fmt.Println("Be patient...")
	}
	//////////////////////////////////
	enoughRobbers := false
	enoughBags := true

	// Menggunakan operator ||
	if enoughRobbers || enoughBags {
		fmt.Println("Grab everything!")
	} else {
		fmt.Println("Grab whatever you can!")
	}
	//////////////////////////////////
	// Menggunakan operator !
	readyToGo := true
	if !readyToGo { // karena pada kondisi ini kita tambahkan ! maka akan menghasilkan nilai false dan yang akan
		fmt.Println("Start the car!") // dieksekusi itu adalah "What are we waiting for??"
	} else {
		fmt.Println("What are we waiting for??")
	}
	// Sebelumnya bahwa kita belajar mengenai else if (elif) tetapi jika kita terus ingin mengecek kondisi lain
	// yang sangat banyak cukup melelahkan bagi kita dan program kita juga nah opsi yang lebih cepat adalah
	// dengan menggunakan Switch.
	// Switch adalah sebuah kondisi yang menentukan kondisi mana yang akan dieksekusi.
	// dan nanti didalam Switch kita bisa menambahkan kondisi lainnya yang dibutuhkan. dan namanya yaitu case
	// dimana case digunakan untuk menambahkan kondisinya.
	// kemudian bagaimana jika case yang ditambahkan didalam switch itu tidak memenuhi kondisi yang diinginkan
	// kita dapat menambahkan default case yang akan dieksekusi jika tidak ada case yang memenuhi kondisi yang diinginkan.
	// Contoh:
	clothingChoice := "sweater"

	switch clothingChoice {
	case "shirt":
		fmt.Println("We have shirts in S and M only.")
	case "polos":
		fmt.Println("We have polos in M, L, and XL.")
	case "sweater":
		fmt.Println("We have sweaters in S, M, L, and XL.")
	case "jackets":
		fmt.Println("We have jackets in all sizes.")
	default: // Nilai default jika case yang ditambahkan tidak memenuhi kondisi yang diinginkan
		fmt.Println("Sorry, we don't carry that")
	}
	// Prints: We have sweaters in S, M, L, and XL.
	// Kemudian ada cara bagaimana menulis if else statement dan switch statement yang lebih singkat.
	// singkat dalam artinya kita bisa mendefinisikan variable nya di dalam if else statement dan switch statement.
	// Contoh:
	if success := true; success{ // cara penulisannya => if <deklarasi variabel>; <kondisi> {}
		fmt.Println("We're rich!")
	} else {
		fmt.Println("Where did we go wrong?")
	}
	amountStolen := 50000
	switch numOfThieves := 5; numOfThieves { // cara penulisannya => switch <deklarasi variabel>; <kondisi> {}
	case 1:
		fmt.Println("I'll take all $", amountStolen)
	case 2:
		fmt.Println("Everyone gets $", amountStolen/2)
	case 3:
		fmt.Println("Everyone gets $", amountStolen/3)
	case 4:
		fmt.Println("Everyone gets $", amountStolen/4)
	case 5:
		fmt.Println("Everyone gets $", amountStolen/5)
	default:
		fmt.Println("There's not enough to go around...")
	}

	// Kemudian pada golang juga ada yang namanya modul untuk random angka loh. yaitu rand.Intn() <= nama fungsinya.
	// Contoh:
	amountLeft := rand.Intn(10000) // <= FUNGSI rand.Intn(Maksimum angka/batasannya) menghasilkan angka random
	fmt.Println("amountLeft is: ", amountLeft) //  tetapi angkanya kurang dari 10000
	if amountLeft > 5000 {
			fmt.Println("What should I spend this on?")
	} else {
		fmt.Println("Where did all my money go?")
	}
	// nah selain itu jika kita menggunakan random math kita bisa gabungkan dengan modul time loh. dimana
	// yang nantinya akan di kombinasikan sehingga akan menghasilkan nilai benih unik yang didapatkan karena
	// gabungan dengan waktu. sebelum itu kita harus menambahkan modul time.
	// Contoh:
	rand.Seed(time.Now().UnixNano()) // Mencari nilai benih random dengan menggabungkan waktu dan Nano detik
	amountLeftright := rand.Intn(10000) // 
	fmt.Println("amountLeft is: ", amountLeftright) // 
	if amountLeftright > 5000 {
			fmt.Println("What should I spend this on?")
	} else {
		fmt.Println("Where did all my money go?")
	}
}