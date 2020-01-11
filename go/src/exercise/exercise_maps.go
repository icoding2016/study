/* Exercise: Maps
Implement WordCount.
It should return a map of the counts of each “word” in the string s.
The wc.Test function runs a test suite against the provided function and prints success or failure.

You might find strings.Fields helpful.
*/

//package main
package exercise

import (
	"fmt"
	"strings"
	//"golang.org/x/tour/wc"
)

// WordCount : count the words in a string and return a map
func WordCount(s string) map[string]int {

	var m map[string]int

	words := strings.Fields(s)

	m = make(map[string]int, len(words))

	for _, w := range words {
		_, ok := m[w]
		if ok != true {
			m[w] = 1
		} else {
			m[w]++ // m[w] += 1 should be replaced with m[w]++
		}
	}
	return m
}

func Exer_Map() {
	example := "I hate burger, but I will eat 2 bugers since there is nothing else to eat."

	m := WordCount(example)
	fmt.Printf("%v", m)
}
