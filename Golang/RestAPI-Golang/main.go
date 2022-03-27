// Restfull API Golang
package main

import (
	"fmt"
	//"net/http"
)

type Food struct { // => class object
	ID 			int
	Nama 	  	string
	Catergory 	string
}


func main(){
	fmt.Println("Hello World")

	//log.Fatal(http.ListenAndServe(":8000", nil)) // => listen port 8000


}