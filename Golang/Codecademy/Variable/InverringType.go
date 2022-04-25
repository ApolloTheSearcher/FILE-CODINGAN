package main
import "fmt"
// Cara yang kita gunakan untuk mendeklarasikan suatu variable tanpa menggunakan tipe data atau mengganti
// nilai di dalam variable sebelumnya
/*
Penjelasan lebih terperinci
Ada cara untuk mendeklarasikan variabel tanpa secara eksplisit menyatakan tipenya menggunakan := operator
deklarasi pendek. Kita mungkin menggunakan := operator jika kita tahu nilai apa yang kita ingin variabel kita
simpan saat membuatnya.

Kami menggunakan :=untuk membuat variabel dan menyimpulkan tipenya berdasarkan nilai yang diberikan.
*/


func main(){
	dayOnVacation := 20
	fmt.Println(dayOnVacation)
}

func Ada(){
	  // Define cupsOfCoffeeConsumed here
	var cupsOfCoffeeConsumed int // Default int variable cara kita
	/*
	Jika kita menggunakan int saja atau jenis datanya tanpa mendeklarasikan berapa besarnya
	maka itu akan disebut default int variable dimana nanti dari Golangnya akan menyesuaikan besar byte memori
	yang digunakannya.

	Pada jenis type data default variable angka kita dapat menggunakan int dan uint untuk menyimpan nilai
	jika kita menggunakan int atau uint itu sizenya 32 bit atau 64 bit tergantung dari jenis komputenya.
	*/
	  // Give a value to cupsOfCoffeeConsumed
	cupsOfCoffeeConsumed = 10
	  // Print out cupsOfCoffeeConsumed
	fmt.Println(cupsOfCoffeeConsumed)
}

// Cara memperbarui nilai dari variable
/*
Kita dapat memperbarui nilai dari variable dengan cara menggunakan keyword "=" dan nilai dari variable tidak
boleh constans. dan operator := itu kunci jika kita ingin memperbarui nilai dari variable.
Contoh programnya :
*/
func Update() {
	coolSneakers := 65.99
	niceNecklace := 45.50

  	// Define taxCalculation here	
	var taxCalculation float64

	// Add coolSneakers to taxCalculation
	taxCalculation += coolSneakers 

  	// Add niceNecklace to taxCalculation
	taxCalculation += niceNecklace

  	// Compute the NYC sales tax
  	// 8.875% of the purchase here:
	taxCalculation *= .08875
  	// Uncomment this line for a receipt!
	fmt.Println("Purchase of", coolSneakers + niceNecklace, "with 8.875 % sales tax", taxCalculation, "equal to", coolSneakers + niceNecklace + taxCalculation)
}