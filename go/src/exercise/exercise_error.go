/*
Exercise: Errors
Copy your Sqrt function from the earlier exercise and modify it to return an error value.

Sqrt should return a non-nil error value when given a negative number, as it doesn't support complex numbers.

Create a new type

type ErrNegativeSqrt float64
and make it an error by giving it a

func (e ErrNegativeSqrt) Error() string
method such that ErrNegativeSqrt(-2).Error() returns "cannot Sqrt negative number: -2".

Note: A call to fmt.Sprint(e) inside the Error method will send the program into an infinite loop. You can avoid this by converting e first: fmt.Sprint(float64(e)). Why?

Change your Sqrt function to return an ErrNegativeSqrt value when given a negative number.

https://tour.golang.org/methods/20
*/

//package main
package exercise

import (
	"fmt"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("Error: Negative value %v cannot do Sqrt.", float64(e))
	// Note: A call to fmt.Sprint(e) inside the Error method will send the program into an infinite loop.
	// You can avoid this by converting e first: fmt.Sprint(float64(e)).
}

func Sqrt(x float64) (float64, error) {
	var z = float64(1)
	const GAP = 0.01

	errNegativeSqrt := ErrNegativeSqrt(x)
	if x < 0 {
		return 0, errNegativeSqrt
	}

	for gap_abs := GAP; gap_abs >= GAP; {
		gap := z*z - x
		if gap < 0 {
			gap_abs = -gap
		} else {
			gap_abs = gap
		}
		z -= gap / (2 * z)
		//fmt.Println(z)
	}
	return z, nil
}

func Exer_Error() {
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(-2))
}
