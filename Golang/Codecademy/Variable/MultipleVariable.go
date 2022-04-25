package main
import "fmt"

/*
Kita juga dapat mendeklarasi sebuah variable ganda atau bisa mendeklarasikan variable ganda dengan satu typedata
Contoh Program:

*/

func main(){
	  // Define magicNum and powerLevel below:
	var magicNum, powerLevel int32 // Multiple variable declaration dengan operator = dan menggunakan var
	magicNum = 2048
	powerLevel = 9001

	fmt.Println("magicNum is:", magicNum, "powerLevel is:", powerLevel)
	  // Define amount and unit below:
	amount, unit := 10, "doll hairs" // Multiple variable declaration dengan operator ':='
	fmt.Println(amount, unit, ", that's expensive...")

}