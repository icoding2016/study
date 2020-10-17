package exercise

import (
	"fmt"
	"errors"
)


type Stack interface {
	Push(*BTreeNode) (*BTreeNode, error)
	Pop() (BTreeNode, error)
}

type BTreeNodes []BTreeNode

// Push a tree node to the stack
func (pns *BTreeNodes) Push(n *BTreeNode) error {
	ns := append(*pns, *n)
	fmt.Printf("ns: %v\n", ns)
	* pns = ns
	return nil
}

// Pop the latest item out of the queue of BTreeNode
func (pns *BTreeNodes) Pop() (BTreeNode, error) {
	var node BTreeNode

	if len(*pns) == 0 {
		return node, errors.New("Queue is empty")
	}
	node, *pns = (*pns)[len(*pns)-1], (*pns)[:len(*pns)-1]
	return node, nil
}


func TestBTreeStack() {
	var tns BTreeNodes
	l := []int{1,2,3,4,5,6}
	for _,v := range(l) {
		node := BTreeNode{v, nil, nil}
		tns.Push(&node)
	}
	fmt.Printf("%v", tns)

	for node, err := tns.Pop(); err == nil; node, err = tns.Pop() {
		fmt.Printf("%v\n", node)
	}

	
}
