/*
https://www.hackerrank.com/challenges/30-arrays/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Input Format
The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers describing array A's elements.

Constraints
- 1<=N<=1000
- 1<=Ai<=10000, where A is the  integer in the array.

Output Format
Print the elements of array A in reverse order as a single line of space-separated numbers.

Sample Input
4
1 4 3 2

Sample Output
2 3 4 1

*/

package exercise

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func TestArray() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024*10)

	nTemp, err := strconv.ParseInt(testArrayReadLine(reader), 10, 64)
	testArrayCheckError(err)
	n := int32(nTemp)

	arrTemp := strings.Split(testArrayReadLine(reader), " ")

	var arr []int32

	for i := 0; i < int(n); i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		testArrayCheckError(err)
		arrItem := int32(arrItemTemp)
		arr = append(arr, arrItem)
	}
	for i := 0; i < len(arr); i++ {
		fmt.Printf("%v ", arr[n-int32(i)-1])
	}
}

func testArrayReadLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func testArrayCheckError(err error) {
	if err != nil {
		panic(err)
	}
}
