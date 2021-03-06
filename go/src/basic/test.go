package basic

import (
	"fmt"
	"math"
	"math/cmplx"
	"runtime"
)

// PI : constant value for Pi
const PI = 3.141592653589793238

var g, c, p bool = true, false, false

var (
	// ToBe : an exportable varible in package basic
	ToBe bool = false
	// MaxInt : an exportable varible in package basic
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func add(x, y int) int {
	return x + y
}

func swap(x, y string) (string, string) {
	return y, x
}

func half(sum int) (x, y int) {
	x = sum / 2
	y = sum - x
	return // 'naked' return, allowed but only for short function considering readability
}

func loopSum(a int) int {
	sum := 0
	for i := 0; i < a; i++ {
		sum += i
	}
	return sum
}

func loop(a int) int {
	sum := 1
	for sum < a {
		sum += sum
	}
	return sum
}

func sqrt(x float64) string {
	if x < 0 {
		return fmt.Sprintf("%v + i", math.Sqrt(-x))
	}
	return fmt.Sprint(math.Sqrt(x))
}

// Sqrt : local version of Sqrt function
func Sqrt(x float64) float64 {
	var z = float64(1)
	const GAP = 0.01

	for gapAbs := GAP; gapAbs >= GAP; {
		gap := z*z - x
		if gap < 0 {
			gapAbs = -gap
		} else {
			gapAbs = gap
		}
		z -= gap / (2 * z)
	}
	return z
}

func getOS() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
}

func showVar() {
	fmt.Printf("Type: %T, Value: %v \n", ToBe, ToBe)
	fmt.Printf("Type: %T, Value: %v \n", MaxInt, MaxInt)
	fmt.Printf("Type: %T, Value: %v \n", z, z)
}

func typeOpr() {
	var i int = 100
	var f float64 = float64(i)
	var u uint = uint(f) // u := uint(f)

	fmt.Println(f / 3)
	fmt.Println(u)
}

func test() {
	Hello()
	TestExport()

	var i int = 1
	fmt.Printf("%v, %v, %v, %v", i, g, c, p)

	showVar()
}
