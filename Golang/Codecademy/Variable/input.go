package main
import "fmt"

func main(){
	// Disini kita akan membahas bagaimana cara membuat input pada bahasa golang
	// Yaitu dengan menggunakan fmt.Scan() tetapi didalam Scan terdapat operator & yang digunakan untuk
	// Input
	// fmt.Scan(&variable)
	// Contoh:
	fmt.Println("What would you like for lunch?")
	// Add your code below:
	var food string
	fmt.Scan(&food) // Input
	fmt.Printf("Sure, we can have %v for lunch.", food)
	// Atau
	fmt.Println("How are you doing?") 
	var response1 string 
	var response2 string 
	fmt.Scan(&response1)
	fmt.Scan(&response2)
	fmt.Printf("I'm %v %v", response1, response2)
}