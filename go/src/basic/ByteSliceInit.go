package basic

import (
	"fmt"
)

type Bbuf []byte
type Bbufs []Bbuf

func ByteSliceInit() {

	var b1 Bbuf = []byte{'x', 'y', 'z'}
	var b2 Bbuf = []byte("opq")
	var bs1 Bbufs = []Bbuf{[]byte("abc"), []byte("efg"), []byte("rjk")}

	//var buf []byte = []byte{'a','b','c'}
	//buf.MyBAppend(b1)

	fmt.Println(b1)
	fmt.Printf("%T\n", b1)
	fmt.Printf("%T\n", bs1)

	fmt.Println(b2)
	fmt.Println(bs1)

	//var buf1 Bbuf = []byte{"Bbuf-Initial-value"}
	//fmt.Fprint(buf1, "something else.")
	//fmt.Println(buf1)
}
