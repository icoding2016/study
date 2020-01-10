package exercise

import (
	"errors"
	"fmt"
)

// Node a struct holding an int value
type Node struct {
	value int
}

// type tree struct {
// 	root *Node
// }

// Nodes is a queue for Node object
type Nodes []Node

// Push a node to the queue of Nodes
func (pns *Nodes) Push(n *Node) (*Nodes, error) {
	ns := append(*pns, *n)
	fmt.Printf("ns: %v", ns)
	pns = &ns
	return pns, nil
}

// Pop the latest item out of the queue of Nodes
func (pns *Nodes) Pop() (Node, error) {
	var node Node

	if len(*pns) == 0 {
		return node, errors.New("Queue is empty")
	}
	node, *pns = (*pns)[len(*pns)-1], (*pns)[:len(*pns)-1]
	return node, nil
}

// TestPushPop ..
func TestPushPop() {
	l := []int{5, 2, 3, 8, 6, 1, 4, 9, 7, 10}
	ns := Nodes{}
	pns := &ns

	fmt.Printf("ns=%v", ns)

	for _, v := range l {
		node := &Node{v}
		//node.value = v
		p, err := pns.Push(node)
		pns = p
		if err == nil {
			fmt.Printf("%v pushed to Nodes, now len=%v\n", node, len(*pns))
		}
	}

	fmt.Printf("%v", pns)
	fmt.Println("-------------------")

	for n, err := pns.Pop(); err == nil; n, err = pns.Pop() {
		fmt.Printf("Pop %v from Nodes\n", n)
	}
	fmt.Println("-------------------")

}
