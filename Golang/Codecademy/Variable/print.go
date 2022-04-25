package main
import "fmt"

func main(){
	// Method Print
	// pada sebuah bahasa golang terdapat fungsi print lagi selain Println yaitu Print yang digunakan untuk
	// menyambungkan string dengan string lainnya jadi contoh:
	fmt.Print("Hello ")
	fmt.Print("World")
	// Output: Hello World karena dia tidak menggunakan println jadi dia akan ngeprint string sesuai dengan
	// fungsinya.
	// Method Printf
	// Printf adalah suatu cara fungsi print yang digunakan untuk formatting dengan menggunakan operator %v
	// format suatu nilai variable di masukan kedalam Printf
	// Contoh:
	animal1 := "cat"
	animal2 := "dog"
	fmt.Printf("Are you a %v or a %v person?", animal1, animal2) // Output: Are you a cat or a dog person?
	// Diatas adalah program yang digunakan untuk menampilkan string dengan format yang ditentukan.
	// selain operator %v yang digunakan untuk menampilkan nilai variable. kita juga bisa menggunakan operator
	// %T untuk menampilkan tipe data dari variable yang dimasukan kedalam variable.
	// Contoh:
	specialNum := 42
	fmt.Printf("This value's type is %T.", specialNum)
	// Prints: This value's type is int.

	quote := "To do or not to do"
	fmt.Printf("This value's type is %T.", quote)
	// Prints: This value's type is string.
	// Selain itu ada pada fungsi Printf dengan operator %d yang digunakan untuk merubah nilai data menjadi
	// string.
	// Contoh:
	votingAge := 18
	fmt.Printf("You must be %d years old to vote.", votingAge)
	// Prints: You must be 18 years old to vote. 
	// Kemudian jika kita ingin menggunakan float kita dapat menggunaka operator %f
	// dimana fungsinya itu untuk mendeklarasi angka di belakang koma
	// Contoh:
	gpa := 3.8
	fmt.Printf("You're averaging: %f.", gpa)
	// Prints: You're averaging 3.800000.
	gpas := 3.8
	fmt.Printf("You're averaging: %.2f.", gpas)
	// Prints: You're averaging 3.80.

	// Kemudian kita sebelumnya telah membahas mengenai Print dan Printl
	// tetapi jika kalian tahu bahwa bahasa golang terdapat fungsi yang bernama Sprint dan Sprintln
	// dimana kegunaanya hampir sama dengan Print dan Println tetapi jika Sprint itu digunakan untuk
	// disimpan di variable. Jika kita menggunakan Sprint maka kita dapat membuat suatu string menjadi beberapa
	// dalam satu baris
	// Jika kita menggunakan Sprintln maka kita hanya dapat mengeluarkan hasilnya sebaris itu
	// dan operator yang digunakan := untuk menyimpan nilai dari Sprint dan Sprintln
	// Contoh:
	// Menggunakan Sprint
	grade := "100"
	compliment := "Great job!"
	teacherSays := fmt.Sprint("You scored a ", grade, " on the test! ", compliment)
	fmt.Print(teacherSays)
	// Prints: You scored a 100 on the test! Great job!
	// Menggunakan Sprintln
	quote = fmt.Sprintln("Look ma,", "no spaces!")
	fmt.Print(quote) // Prints Look ma, no spaces!
	// Tetapi selain itu ada yang namanya itu Sprintf yang fungsinya sama dengan Printf namun dia digunakan
	// untuk menyimpan nilai dari Sprintf kedalam variable.
	// Contoh:
	correctAns := "A"
	answer := fmt.Sprintf("And the correct answer is… %v!", correctAns)
	fmt.Print(answer) // Prints: And the correct answer is… A!
	// Atau
	template := "I wish I had a %v."
	pet := "puppy"
	var wish string
	// Add your code below:
	wish = fmt.Sprintf(template, pet)
	fmt.Println(wish)
	// Prints: I wish I had a puppy.
}