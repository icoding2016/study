/*
Exercise: Fibonacci closure
Implement a fibonacci function that returns a function (a closure) that returns successive fibonacci numbers (0, 1, 1, 2, 3, 5, ...).
*/

//package main
package exercise

import "fmt"

var x int = -1
var y int = -1

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {

	return func() int {
		if x == -1 {
			x = 0
			return x
		}
		if y == -1 {
			y = 1
			return y
		}

		var cur int = x + y
		x = y
		y = cur
		return cur
	}

}

func Exer_FibonacciClosure() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
