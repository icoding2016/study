/*
https://www.hackerrank.com/challenges/30-hello-world/problem
https://www.hackerrank.com/challenges/30-data-types/problem?h_r=next-challenge&h_v=zen
*/

package exercise

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

// TestReader exercises the bufio.Reader function
func TestReader() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT

	reader := bufio.NewReader(os.Stdin)
	txt, _ := reader.ReadString('\n')
	txt = strings.Replace(txt, "\n", "", -1)
	fmt.Println(txt)
}

// TestScanner exercises the bufio.Scanner function
func TestScanner() {
	var _ = strconv.Itoa // Ignore this comment. You can still use the package "strconv".
  
    var i uint64 = 4
    var d float64 = 4.0
    var s string = "HackerRank "

    scanner := bufio.NewScanner(os.Stdin)
    // Declare second integer, double, and String variables.
    var ii uint64
    var dd float64
    var ss string
    // Read and save an integer, double, and String to your variables.
    lineCounter := 0
    for scanner.Scan() {
        switch lineCounter {
            case 0:
                ii, _ = strconv.ParseUint(scanner.Text(), 10, 64)
            case 1:
                dd, _ = strconv.ParseFloat(scanner.Text(), 64)
            case 2:
                ss = scanner.Text()
        }
        lineCounter += 1
    }
    
    // Print the sum of both integer variables on a new line.
    fmt.Println(ii + i)
    
    // Print the sum of the double variables on a new line.
    fmt.Printf("%.1f\n", dd + d)
    
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    fmt.Println(s + ss)

}


func TestScanner1() {
	const inputTxt string = `12
3.14
An example string.`

	var i uint64 = 4
	var d float64 = 4.0
	var s string = "HackerRank "

	var _ = strconv.Itoa // Ignore this comment. You can still use the package "strconv".

	var ii uint64
    var dd float64
    var ss string

	scanner := bufio.NewScanner(strings.NewReader(inputTxt))
    lineCounter := 0
    for scanner.Scan() {
        switch lineCounter {
            case 0:
                ii, _ = strconv.ParseUint(scanner.Text(), 10, 64)
            case 1:
                dd, _ = strconv.ParseFloat(scanner.Text(), 64)
            case 2:
                ss = scanner.Text()
        }
        lineCounter += 1
    }

	fmt.Println(ii + i)
    fmt.Printf("%.2f\n", dd + d)
    fmt.Println(s + ss)

}
