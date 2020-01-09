/*
Define a func btree(d []int,) Tree, where inInsert
  d:  a list of values,
  return: the root of the tree (a Tree structure) which is created based on the sequence of d

*/

package exercise

import (
	"fmt"
)

// BTree a Binary Tree Struct
type BTree struct {
	value int
	left  *BTree
	right *BTree
}

type btreeLevel struct {
	lOpen bool
	rOpen bool
}

type levels []btreeLevel

// Insert a value in the binary tree (lower to left, higher to right)
//   t: current BTree node
//   return: (node, parent)
//            node - the pointer to the BTree node where the new value is Inserted at,
//            parent - the pointer to parent BTree node
func (t *BTree) Insert(value int) (*BTree, *BTree) {
	if t == nil {
		//fmt.Printf("Create new tree-node from %v(%v), value=%v\n", nil, nil, value)
		//t := new(BTree)
		//t.value = value
		return nil, nil
	}

	var n *BTree = nil
	var p *BTree = nil

	if value < t.value {
		fmt.Printf("Go left node from %v(%v)->left for inserting %v\n", t, t.value, value)
		if t.left != nil {
			n, p = t.left.Insert(value)
		} else {
			t.left = new(BTree)
			t.left.value = value
			return t.left, t
		}

	} else if value > t.value {
		fmt.Printf("Go right node from %v(%v)->right for inserting %v\n", t, t.value, value)
		if t.right != nil {
			t.right.Insert(value)
		} else {
			t.right = new(BTree)
			t.right.value = value
			return t.right, t
		}
	} else {
		// same value, ignore
		return t, nil
	}
	return n, p
}

// Show walk throught the tree and display the value
//   t: current node
//   return: parent node
func (t *BTree) Show() {
	if t == nil {
		return
	}
	fmt.Printf("[%v]", t.value)
	fmt.Printf("\tleft->")
	if t.left == nil {
		fmt.Printf("nil")
	} else {
		fmt.Printf("%v", t.left.value)
	}
	fmt.Printf("\tright->")
	if t.right == nil {
		fmt.Printf("nil\n")
	} else {
		fmt.Printf("%v\n", t.right.value)
	}

	t.left.Show()
	t.right.Show()
}

// Draw walk throught the tree and display the tree structure
//   t: current node
func (t *BTree) Draw() {
	if t == nil {
		return
	}
	fmt.Printf("[%v]", t.value)
	fmt.Printf("\tleft->")
	if t.left == nil {
		fmt.Printf("nil")
	} else {
		fmt.Printf("%v", t.left.value)
	}
	fmt.Printf("\tright->")
	if t.right == nil {
		fmt.Printf("nil\n")
	} else {
		fmt.Printf("%v\n", t.right.value)
	}

	t.left.Draw()
	t.right.Draw()
}

// New generate a BTree based on the inInsert list of value (by the order of the sequence)
func (t *BTree) New(d []int) *BTree {
	if len(d) == 0 {
		return nil
	}

	root := t // point to parent node
	root.value = d[0]
	p := root
	for _, v := range d[1:] {
		_, p = root.Insert(v)
		fmt.Printf("%v inserted under %v\n", v, p)
	}
	return root
}

//////////////////

// func (l *levels) append(ls *levels, bl *btreeLevel) {
// 	if len(ls)+1 > cap(ls) {
// 		nls = make([]btreeLevel, cap(ls)+1)
// 		nls[:len(ls)] = ls[:len(ls)]
// 		for i := 0; i < cap(ls); i++ {
// 			ls[i] = nil
// 		}

// 	}
// }

// func (l levels) Push(n btreeLevel) int {
// 	l = append(l, n)
// 	return len(l)
// }

// func (l levels) Pop(n btreeLevel) (btreeLevel, error) {
// 	if len(l) == 0 {
// 		return nil, errors.New("Fails to pop from an empty queue.")
// 	}
// 	n, l = l[len(l)-1], l[:len(l)-1]
// 	return n, nil
// }
