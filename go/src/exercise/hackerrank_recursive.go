/*
Hackerrank Day 9: Recursive
https://www.hackerrank.com/challenges/30-recursion/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Task
Write a factorial function that takes a positive integer,  as a parameter and prints the result of  ( factorial).

  factorial(N) = / 1                     N<=1
				 \ N * factorial(N-1)    otherwise

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

Input Format
A single integer, N (the argument to pass to factorial).

Constraints
- 2<=N<=12
- must contain a recursive function named factorial

Output Format
Print a single integer denoting N!.

*/

package exercise

import (
	"fmt"
)

// Complete the factorial function below.
func factorial(n int32) int32 {
	if n <= 1 {
		return 1
	} else {
		return factorial(n-1) * n
	}
}

func TestRecursive() {
	testInput := 5

	n := int32(testInput)

	result := factorial(n)

	fmt.Printf("%d\n", result)
}

/*
Online solution:


package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

// Complete the factorial function below.
func factorial(n int32) int32 {
    if n <= 1 {
        return 1
    } else {
        return factorial(n-1) * n
    }
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 1024 * 1024)

    nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
    checkError(err)
    n := int32(nTemp)

    result := factorial(n)

    fmt.Fprintf(writer, "%d\n", result)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}

*/
