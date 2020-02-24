/*
Exercise: Equivalent Binary Trees
There can be many different binary trees with the same sequence of values stored in it.
For example, here are two binary trees storing the sequence 1, 1, 2, 3, 5, 8, 13.
           3                              8
		 /   \                           / \
        1     8                         3   13
       / \   / \                       / \
      1   2  5  13                    1   5
                                     /  \
                                    1    2

A function to check whether two binary trees store the same sequence is quite complex in most languages.
We'll use Go's concurrency and channels to write a simple solution.

This example uses the tree package, which defines the type:
type Tree struct {
    Left  *Tree
    Value int
    Right *Tree
}

1. Implement the Walk function.
2. Test the Walk function.

The function tree.New(k) constructs a randomly-structured (but always sorted) binary tree holding the values k, 2k, 3k, ..., 10k.

Create a new channel ch and kick off the walker:

go Walk(tree.New(1), ch)
Then read and print 10 values from the channel. It should be the numbers 1, 2, 3, ..., 10.

3. Implement the Same function using Walk to determine whether t1 and t2 store the same values.

4. Test the Same function.

Same(tree.New(1), tree.New(1)) should return true, and Same(tree.New(1), tree.New(2)) should return false.

The documentation for Tree can be found here (https://godoc.org/golang.org/x/tour/tree#Tree).


*/

package exercise

import (
	"fmt"

	"golang.org/x/tour/tree"
)

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int) {
	if t == nil {
		return
	}
	if t.Left != nil {
		Walk(t.Left, ch)
	}
	ch <- t.Value
	if t.Right != nil {
		Walk(t.Right, ch)
	}
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {
	var ch1 chan int = make(chan int, 10)
	var ch2 chan int = make(chan int, 10)
	var v1 int
	var v2 int

	go Walk(t1, ch1)
	go Walk(t2, ch2)

	for i := 0; i < 10; i++ {
		v1 = <-ch1
		v2 = <-ch2
		if v1 != v2 {
			return false
		}
	}
	return true

}

func TestEBtreeLib() {
	t11 := tree.New(1)
	t12 := tree.New(1)
	t2 := tree.New(2)
	fmt.Println(t11.String())
	fmt.Println(t12.String())
	fmt.Println(t2.String())

	r1 := Same(tree.New(1), tree.New(1))
	r2 := Same(tree.New(1), tree.New(2))
	fmt.Println(r1)
	fmt.Println(r2)
}
