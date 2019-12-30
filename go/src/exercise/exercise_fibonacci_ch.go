/*
  The 'channel' version of fibonacci
*/

package exercise

import (
	"fmt"
)

// Output fibonacci to channel 'c'
func fibonacci_gen(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func Exer_Fibonacci(n int) {
	c := make(chan int, n)
	go fibonacci_gen(n, c)
	for i := range c {
		fmt.Printf("%v ", i)
	}
}
