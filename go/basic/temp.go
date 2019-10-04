package basic

import (
	"fmt"
	"math"
)

func test_local() {
	s = math.Sqrt(7)
	fmt.Printf("sqrt(7)=%f", s)
}

func Test_export() {
	s = math.Sqrt(7)
	fmt.Printf("sqrt(7)=%f", s)
}
