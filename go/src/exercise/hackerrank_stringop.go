/*
Hackerrank Day 6: Let's Review.
https://www.hackerrank.com/challenges/30-review-loop/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


Task
Given a string S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line
Note: 0 is considered to be an even index.

Input Format
The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a String S.

Constraints
- 0 <= T <= 10
- 2 <= leghth of S <= 10000

Output Format
For each String Sj (where 0<=j<=T-1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak

*/

package exercise

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var testStrOp_input = []string{"3", ""}

func isEven(n uint64) bool {
	var fn float64 = float64(n)

	if fn/2 == float64(n/2) {
		return true
	}
	return false
}

func TestStrOp() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	reader := bufio.NewReader(os.Stdin)

	input, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println("ReadString failed,", err)
		return
	}
	if len(input) <= 1 { // len(input) includes '\n'
		fmt.Println("Empty input", input)
		return
	}
	n, _ := strconv.Atoi(input[:len(input)-1])
	for i := 0; i < n; i++ {
		var se string = ""
		var so string = ""
		ss, _ := reader.ReadString('\n')
		//fmt.Println(ss)
		ll := len(ss)
		if ss[ll-1] == '\n' {
			ll--
		}
		for i := 0; i < ll; i++ {
			x := ss[i]
			if isEven(uint64(i)) {
				se = se + string(x)
			} else {
				so = so + string(x)
			}
		}
		fmt.Printf("%v %v\n", se, so)
	}
}
