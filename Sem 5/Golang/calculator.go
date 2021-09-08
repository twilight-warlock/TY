package main

import "fmt"

func menu() {
	running := true

	for running {
		var n1, n2 int
		var operation int

		response := 0
		result := 0

		fmt.Println("Enter number 1: ")
		fmt.Scanln(&n1)

		fmt.Println("Enter number 2: ")
		fmt.Scanln(&n2)

		fmt.Println("Select an operation")
		fmt.Println("1. Addition")
		fmt.Println("2. Subtraction")
		fmt.Println("3. Multiplication")
		fmt.Println("4. Division")

		fmt.Println("Input:")
		fmt.Scanln(&operation)

		switch operation {
		case 1:
			result = n1 + n2
			break
		case 2:
			result = n1 - n2
			break
		case 3:
			result = n1 * n2
			break
		case 4:
			result = n1 / n2
			break
		default:
			fmt.Println("Invalid Operation")
		}
		fmt.Printf("Result = %d", result)

		fmt.Println("\nDo you want to continue? (0 for no, 1 for yes)")
		fmt.Scanln(&response)

		if response != 1 {
			running = false
		}
	}

}

func main() {

	fmt.Println("Calculator - 1914078")
	menu()

}