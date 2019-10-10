/*
Task
Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:

Declare  variables: one of type int, one of type double, and one of type String.
Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
Use the  operator to perform the following operations:
Print the sum of  plus your int variable on a new line.
Print the sum of  plus your double variable to a scale of one decimal place on a new line.
Concatenate  with the string you read as input and print the result on a new line.


Sample Input
12
4.0
is the best place to learn and practice coding!

Sample Output
16
8.0
HackerRank is the best place to learn and practice coding!

*/

package lessons

import (
	"bufio"
	"fmt"
	"os"
)

// L1_DataType : Lesson1 task
func L1_DataType() {
	var i uint64 = 4
	var d float64 = 4.0
	var s string = "HackerRank "

	scanner := bufio.NewScanner(os.Stdin)

	var ii = scanner.Scan()
	fmt.Println(i)
}
