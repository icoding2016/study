/*
Class vs. Instance
https://www.hackerrank.com/challenges/30-class-vs-instance/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

*/

package exercise

import "fmt"

type person struct {
	age int
}

func (p person) NewPerson(initialAge int) person {
	//Add some more code to run some checks on initialAge
	if initialAge < 0 {
		fmt.Println("Age is not valid, setting age to 0.")
		p.age = 0
	} else {
		p.age = initialAge
	}
	return p
}

func (p person) amIOld() {
	//Do some computation in here and print out the correct statement to the console
	if p.age < 13 {
		fmt.Println("You are young.")
	} else if p.age < 18 {
		fmt.Println("You are a teenager.")
	} else {
		fmt.Println("You are old.")
	}

}

func (p person) yearPasses() person {
	//Increment the age of the person in here
	p.age++
	return p
}

// TestClassInstance test entry of Hackerank class 4
func TestClassInstance() {
	var T, age int

	fmt.Scan(&T)

	for i := 0; i < T; i++ {
		fmt.Scan(&age)
		p := person{age: age}
		p = p.NewPerson(age)
		p.amIOld()
		for j := 0; j < 3; j++ {
			p = p.yearPasses()
		}
		p.amIOld()
		fmt.Println()
	}
}

// TestClassInstance1 Local version of test entry of Hackerank class 4
func TestClassInstance1() {
	var testInput = [...]int{4, -1, 10, 16, 18} // fix the size by [...], testInput should be a 'constant'
	var T, age int

	T = testInput[0]

	for i := 0; i < T; i++ {
		age = testInput[i+1]
		p := person{age: age}
		p = p.NewPerson(age)
		p.amIOld()
		for j := 0; j < 3; j++ {
			p = p.yearPasses()
		}
		p.amIOld()
		fmt.Println()
	}
}
