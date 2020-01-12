/*
Define a func BTreeNode(d []int,) Tree, where inInsert
  d:  a list of values,
  return: the root of the tree (a Tree structure) which is created based on the sequence of d

*/

package exercise

import (
	"fmt"
)

// BTreeNode a Binary Tree Struct
type BTreeNode struct {
	value int
	left  *BTreeNode
	right *BTreeNode          
}

type BTreeNodeLevel struct {
	lOpen bool
	rOpen bool
}

type levels []BTreeNodeLevel

// Insert a value in the binary tree (lower to left, higher to right)
//   t: current BTreeNode node
//   return: (node, parent)
//            node - the pointer to the BTreeNode node where the new value is Inserted at,
//            parent - the pointer to parent BTreeNode node
func (t *BTreeNode) Insert(value int) (*BTreeNode, *BTreeNode) {
	if t == nil {
		fmt.Printf("Create new tree-node from %v(%v), value=%v\n", nil, nil, value)
		*t = BTreeNode{value, nil, nil}
		return t, nil
	}

	var pn *BTreeNode
	var pp *BTreeNode

	n := BTreeNode{value, nil, nil}
	//pn = &n

	if value <= t.value {
		fmt.Printf("Go left node from %v(%v)->left for inserting %v\n", t, t.value, value)
		if t.left != nil {
			pn, pp = t.left.Insert(value)
		} else {
			t.left = &n
			return t.left, t
		}

	} else {  //if value > t.value {
		fmt.Printf("Go right node from %v(%v)->right for inserting %v\n", t, t.value, value)
		if t.right != nil {
			pn, pp = t.right.Insert(value)
		} else {
			t.right = &n
			return t.right, t
		}
	}
	return pn, pp
}

// Show walk throught the tree and display the value
//   t: current node
//   return: parent node
func (t *BTreeNode) Show() {
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
func (t *BTreeNode) Draw() {
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

// New generate a BTreeNode based on the inInsert list of value (by the order of the sequence)
func (t *BTreeNode) New(d []int) *BTreeNode {
	if len(d) == 0 {
		return nil
	}

	root := t // point to parent node
	for _, v := range d {
		pn, pp := root.Insert(v)
		if root == nil {
			if pp == nil {
				root = pn
			} else {
				root = pp
			}
		}

		fmt.Printf("%v inserted under %v\n", v, *pp)
	}
	return root
}

