package welcome
import "fmt"
func GreetUsers(ticketName string, ticketCount uint, ticketValue int) (string, uint, int) {
	fmt.Printf("Welcome to our %v\n", ticketName)
	fmt.Println("hello fellas, for", ticketName, " book your ticket here")
	fmt.Println("Total tickets available", ticketCount, "from", ticketValue)
	return ticketName, ticketCount, ticketValue
}
