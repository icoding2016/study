package exercise

import (
	"errors"
	"fmt"
)

type Node struct {
	value int
}

// type tree struct {
// 	root *Node
// }

// Nodes is a queue for Node object
type Nodes []Node

// Push a node to the queue of Nodes
func (ns Nodes) Push(n *Node) (Nodes, error) {
	ns = append(ns, *n)
	fmt.Printf("ns: %v", ns)
	return ns, nil
}

// Pop the latest item out of the queue of Nodes
func (ns Nodes) Pop() (Node, error) {
	var node Node

	if len(ns) == 0 {
		return node, errors.New("Queue is empty")
	}
	node, ns = ns[len(ns)-1], ns[:len(ns)-1]
	return node, nil
}

// TestPushPop ..
func TestPushPop() {
	l := []int{5, 2, 3, 8, 6, 1, 4, 9, 7, 10}
	ns := Nodes{}

	for _, v := range l {
		node := new(Node)
		node.value = v
		ns, err := ns.Push(node)
		if err == nil {
			fmt.Printf("%v pushed to Nodes, now len=%v\n", node, len(ns))
		}
	}

	fmt.Printf("%v", ns)
	fmt.Println("-------------------")

	for n, err := ns.Pop(); err == nil; n, err = ns.Pop() {
		fmt.Printf("Pop %v from Nodes\n", n)
	}

}
