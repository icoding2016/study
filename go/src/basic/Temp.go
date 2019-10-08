package basic

import (
	"fmt"
	"math"
)


func testLocal() {
	s := math.Sqrt(7)
	fmt.Printf("sqrt(7)=%f", s)
}

// TestExport : a example function to be exported
func TestExport() {
	s := math.Sqrt(7)
	fmt.Printf("sqrt(7)=%f", s)
}
