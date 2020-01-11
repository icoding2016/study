package main

import (
	"exercise"
)

func main() {
	// lessons.L0_InOutput()
	//lessons.L1_DataType()
	//exercise.Fibonacci(12)

	//
	//exercise.TestPushPop()
	//
	t := new(exercise.BTree)
	t.New([]int{5, 3, 1, 7, 2, 6, 9})
	//fmt.Println(t)
	t.Show()
}
