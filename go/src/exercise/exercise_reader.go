/*
Exercise: Readers
Implement a Reader type that emits an infinite stream of the ASCII character 'A'.

https://tour.golang.org/methods/22

the io.Reader definition
type Reader interface {
    Read(p []byte) (n int, err error)
}


*/

package exercise

/*
//import "golang.org/x/tour/reader"

type MyReader struct {
	i int // current index
}

// TODO: Add a Read([]byte) (int, error) method to MyReader.

func (mr MyReader) Read(b []byte) (n int, e error) {
	b[0] = 'A'
	mr.i += 1
	return 1, nil
}

func Exer_Reader() {
	r := MyReader{}
	reader.Validate(r)
}

*/
