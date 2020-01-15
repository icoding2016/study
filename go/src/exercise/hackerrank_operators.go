/*
https://www.hackerrank.com/challenges/30-operators/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!
*/

/*
Sample Input
12.00
20
8

Sample Output
15
*/

package exercise

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// Complete the solve function below.
// math.Round() can do the round up work, but we don't use it in this exercise
func solve(meal_cost float64, tip_percent int32, tax_percent int32) {
	cost := meal_cost*float64(tip_percent)/100 + meal_cost*float64(tax_percent)/100 + float64(meal_cost)
	ii := int64(cost)
	gap := cost - float64(ii)
	if gap >= 0.5 {
		gap = 1
	} else {
		gap = 0
	}

	result := ii + int64(gap)
	fmt.Printf("Rounded totalCost = %v\n",result)
}

func opr_readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

// TestOperators the test function
func TestOperators() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	meal_cost, err := strconv.ParseFloat(opr_readLine(reader), 64)
	checkError(err)

	tip_percentTemp, err := strconv.ParseInt(opr_readLine(reader), 10, 64)
	checkError(err)
	tip_percent := int32(tip_percentTemp)

	tax_percentTemp, err := strconv.ParseInt(opr_readLine(reader), 10, 64)
	checkError(err)
	tax_percent := int32(tax_percentTemp)

	solve(meal_cost, tip_percent, tax_percent)
}

// TestOperators1 the alternative version using string input instead of stdio
func TestOperators1() {
	const inputText = `12.00
20
8
`
	reader := bufio.NewReader(strings.NewReader(inputText))

	meal_cost, err := strconv.ParseFloat(opr_readLine(reader), 64)
	checkError(err)

	tip_percentTemp, err := strconv.ParseInt(opr_readLine(reader), 10, 64)
	checkError(err)
	tip_percent := int32(tip_percentTemp)

	tax_percentTemp, err := strconv.ParseInt(opr_readLine(reader), 10, 64)
	checkError(err)
	tax_percent := int32(tax_percentTemp)

	solve(meal_cost, tip_percent, tax_percent)
}
