/*
https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Task
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for name is not found, print "Not found" instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format
The first line contains an integer, n, denoting the number of entries in the phone book.
Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line.
The first value is a friend's name, and the second value is an 8-digit phone number.

After the  lines of phone book entries, there are an unknown number of lines of queries.
Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.

Constraints
- 1<=n<=100000
- 1<=queries<=100000

Output Format
On a new line for each query, print "Not found" if the name has no corresponding entry in the phone book;
otherwise, print the full name and number in the format name=phoneNumber.

Sample Input
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output
sam=99912222
Not found
harry=12299933

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

func TestMap() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024*200)

	line, _, err := reader.ReadLine()
	if err != nil {
		return
	}

	ii, _ := strconv.ParseInt(string(line), 10, 64)

	var phonebook = map[string]string{}

	for i := int64(0); i < ii; i++ {
		line, _, err := reader.ReadLine()
		if err != nil {
			fmt.Printf("Readline error: %v\n", err)
			return
		}
		strArr := strings.Split(string(line), " ")
		name := strArr[0]
		number := strArr[1]
		phonebook[name] = number
	}

	for {
		line, _, err := reader.ReadLine()
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Printf("Readline error: %v\n", err)
			return
		}

		name := string(line)
		phone := phonebook[name]
		if phone == "" {
			fmt.Println("Not found")
		} else {
			fmt.Printf("%v=%v\n", string(line), phone)
		}
	}
	return
}
