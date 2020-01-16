/*
Day 5: Loops
https://www.hackerrank.com/challenges/30-loops/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
*/

package exercise

import (
	// "bufio"
	"fmt"
	// "io"
	// "os"
	// "strconv"
	// "strings"
)

// func readLine(reader *bufio.Reader) string {
// 	str, _, err := reader.ReadLine()
// 	if err == io.EOF {
// 		return ""
// 	}

// 	return strings.TrimRight(string(str), "\r\n")
// }

// func checkError(err error) {
// 	if err != nil {
// 		panic(err)
// 	}
// }

// func TestLoops() {
// 	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

// 	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
// 	checkError(err)
// 	n := int32(nTemp)
// }

func TestLoops1() {
	const testInput = 2

	for i := int32(1); i <= 10; i++ {
		fmt.Printf("%v x %v = %v\n", testInput, i, testInput*i)
	}
}
