package mylib

import (
	"errors"
	"fmt"
)

type T interface{}

// Push an element into a stack
// return non nil error if fail.
func Push(pt *[]T, t T) error {

	if pt == nil {
		n := append(*new([]T), t)
		//p := make([]interface{}, 1);		p[0] = t
		*pt = n
	} else {
		t1 := append(*pt, t)
		*pt = t1
	}
	return nil
}

// Pop an element from a stack
// return non nil error if reach the bottom.
func Pop(pt *[]T) (T, error) {
	var node T
	if pt == nil {
		return node, errors.New("nil pointer (pt)")
	}

	l := len(*pt)
	if l == 0 {
		return node, errors.New("Stack is empty. Nothing to pop")
	}
	node = (*pt)[l-1]
	*pt = (*pt)[:l-1]
	return node, nil
}

// TestStack : a unit test for Stack
func TestStack() {
	ll := []int{1, 2, 3, 4, 5}
	var ss []int

	for _, v := range ll {
		Push(&ss, v)
	}
	fmt.Printf("Stack: %v", ss)

	fmt.Printf("----\n")
}
