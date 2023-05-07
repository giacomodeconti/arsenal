package main

import (
	"fmt"
	"sync"
	"teset-app/welcome"
	"time"
)

var ticketName = "GO conf"
const ticketValue int = 50
var ticketCount uint = 50

// var bookings [50]string -> This is an array, unefficient
var bookings = make([]UserData, 0) // this is slice efficent

var wg = sync.WaitGroup{} // wait for the goroutine to finish

type UserData struct {
	firstName string
	lastName string
	email string
	userTicket uint
}

func main() {

	welcome.GreetUsers(ticketName, ticketCount, ticketValue) // calling funtion

	firstName, lastName, email, userTicket := getUserInputs()

	nameCheck, emailCheck, ticketCheck := ValidInputs(firstName, lastName, email, userTicket)

	if nameCheck && emailCheck && ticketCheck {
		ticketCount = ticketCount - userTicket
		//bookings [0] = firstName + " " + lastName		this is array
	
		var userData = UserData{
			firstName: firstName,
			lastName: lastName,
			email: email,
			userTicket: userTicket,
		}

		wg.Add(1)
		go sendTicket(userTicket, firstName, lastName, email) // with go "goroutine" func create a subprocess of that func so the program can keep running

		bookings = append(bookings, userData) // this is slice
		fmt.Printf("Thank you %v %v you have succesfull booked %v tickets, you will recive an email shortly at %v\n", firstName, lastName, userTicket, email)

		fmt.Printf("%v remaining tickets\n", ticketCount)

		firstNames := []string{}           //slice or dictionary
		// for is a loop, go doesn't have while or similar but only for, here next to the for you can put an condition.
		for _, booking := range bookings { // variable _ is for null and range is range is for create a loop in bookings
			firstNames = append(firstNames, booking.firstName)
		}

		fmt.Printf("These are our bookings: %v\n", firstNames)
		noTicket := ticketCount <= 0
		// If ticket are >0 end program
		if noTicket {
			// end program
			fmt.Println("The event is booked out.")
			//break
		}
		// Error inputs
	} else {
		fmt.Printf("\n---ERRORS:---\n\n")
		if !nameCheck {
			fmt.Println("INVALID NAMES")
		}
		if !emailCheck {
			fmt.Println("INVALID EMAIL")
		}
		if !ticketCheck {
			fmt.Println("INVALID TICKETS")
		}
		fmt.Printf("\n--Try Againg--\n\n")
	}
wg.Wait()
}

// creating a new function

func getUserInputs() (string, string, string, uint) {
	var firstName string
	var lastName string
	var email string
	var userTicket uint

	fmt.Println("Enter your first name: ")
	fmt.Scan(&firstName)

	fmt.Println("Enter your last name: ")
	fmt.Scan(&lastName)

	fmt.Println("Enter your email: ")
	fmt.Scan(&email)

	fmt.Println("Enter number of tickets: ")
	fmt.Scan(&userTicket)

	return firstName, lastName, email, userTicket
}

func sendTicket (userTicket uint, firstName string, lastName string, email string){
	time.Sleep(20 * time.Second) // set a timer for simulate the process
	var ticket = fmt.Sprintf("%v tickets for %v %v", userTicket, firstName, lastName)
	fmt.Println("#################################")
	fmt.Printf("Sending tickets \n%v \nto %v\n", ticket, email)
	fmt.Println("#################################")
	wg.Done()
}

/* here an example the use case of switch commad

city := "London"

switch city {
	case "New York":
		// execute code for booking New York conference tickets
	case "Singapore":
		// execute code for booking Singapore conference tickets
	case "London":
		// execute code for booking London conference tickets
	case "Berlin":
		// execute code for booking Berlin conference tickets
	case "Mexico City":
		// execute code for booking Mexico City conference tickets
	case "Hong Kong":
		// execute code for booking Hong Kong conference tickets
	default:
		fmt.Print("No valid city selected\n")
}

*/
