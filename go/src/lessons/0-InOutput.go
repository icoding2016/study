// Task
// To complete this challenge, you must save a line of input from stdin to a variable, print Hello, World.
// on a single line, and finally print the value of your variable on a second line.

package lessons

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// L0_InOutput : Lesson0 task
func L0_InOutput() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	fmt.Println("Hello, World.")

	reader := bufio.NewReader(os.Stdin)
	txt, _ := reader.ReadString('\n')
	txt = strings.Replace(txt, "\n", "", -1)
	fmt.Println(txt)
}
