package main

// to run inputs.go execute this on terminal: go run main.go inputs.go | or run: go run .   the point is to run all files in the directory.
import "strings"

// function to validate user inputs, nameCheck emailCheck ticketCheck, are not defined so we have to return and specify the output in function, bool bool bool

func ValidInputs(firstName string, lastName string, email string, userTicket uint) (bool, bool, bool) {
	nameCheck := len(firstName) >= 2 && len(lastName) >= 2
	emailCheck := strings.Contains(email, "@")
	ticketCheck := userTicket > 0 && userTicket <= ticketCount
	return nameCheck, emailCheck, ticketCheck
}
