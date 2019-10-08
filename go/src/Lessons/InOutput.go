// Task
// To complete this challenge, you must save a line of input from stdin to a variable, print Hello, World. 
// on a single line, and finally print the value of your variable on a second line.

package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
)

func main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
    fmt.Println("Hello, World.")

    reader := bufio.NewReader(os.Stdin)
    txt, _ := reader.ReadString('\n')
    txt = strings.Replace(txt, "\n", "", -1)
    fmt.Println(txt)
}