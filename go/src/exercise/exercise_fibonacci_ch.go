/*
  The 'channel' version of fibonacci
*/

package exercise

import (
	"fmt"
)

// Output fibonacci to channel 'c' (buffered chan)
func fibonacciGen(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func fibonacci1(n int) {
	c := make(chan int, n)
	go fibonacciGen(n, c)
	for i := range c {
		fmt.Printf("%v ", i)
	}
}

//////////////////

// Output fibonacci to channel 'c' until get signal from 'quit' channel
func fibonacciGen2(c chan int, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			return
		}
	}
}

func fibonacci2(n int) {
	c := make(chan int)
	quit := make(chan int)

	go func() {
		for i := 0; i < n; i++ {
			fmt.Printf("%v ", <-c)
		}
		quit <- 1
	}()

	fibonacciGen2(c, quit)
}

func fibonacci3(n int) {
	c := make(chan int)
	quit := make(chan int)

	go fibonacciGen2(c, quit)
	
	for i := 0; i < n; i++ {
		fmt.Printf("%v ", <-c)
	}
	quit <- 1
}

// Fibonacci : generate a Fibonacci sequence
func Fibonacci(n int) {
	// fibonacci1(n)
	fibonacci3(n)
}
