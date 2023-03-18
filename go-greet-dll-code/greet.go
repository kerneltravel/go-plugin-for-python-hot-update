package main

import "fmt"
import "C"

var V int

//export F
func F() { fmt.Printf("Hello, number \n") }

//func F() { fmt.Printf("Hello, number %d\n", V) }

//export Add
func Add(num1, num2 int) {
	fmt.Printf("%d +%d = %d \n", num1, num2, num1+num2)
}

//export AddResult
func AddResult(num1, num2 int) int {
	return num1 + num2
}

func main() {
	// Need a main function to make CGO compile package as C shared library
}
