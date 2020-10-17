/*
https://www.hackerrank.com/challenges/30-conditional-statements/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.
*/

package exercise

import (
	"bufio"
	"fmt"
	"io"
	"strconv"
	"strings"
)

const testInput = `
1
3
5
7
20
51
`

func isOdd(i int32) bool {
	var f float32
	f = float32(i) / 2
	h := int32(i / 2)
	if f == float32(h) {
		return false
	} else {
		return true
	}
}

func checkNumber(i int32) string {
	if isOdd(i) {
		return "Weird"
	} else if i >= 6 && i <= 20 {
		return "Weird"
	} else { // (i >= 2 && i <= 5) or (i>20)
		return "Not Weird"
	}
}

func cond_readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

// func checkError(err error) {
// 	if err != nil {
// 		panic(err)
// 	}
// }

func TestConditions() {
	//reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)
	reader := bufio.NewReader(strings.NewReader(testInput))

	for Temp, err := strconv.ParseInt(cond_readLine(reader), 10, 64); err == nil; Temp, err = strconv.ParseInt(cond_readLine(reader), 10, 64) {
		N := int32(Temp)
		fmt.Printf("%v -> %v", N, checkNumber(N))
	}
}
