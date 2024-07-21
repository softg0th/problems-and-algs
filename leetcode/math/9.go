package main

import (
	"fmt"
	"strconv"
	"strings"
)

func isPalindrome(x int) bool {
	numStr := strings.Split(strconv.Itoa(x), "")
	digits := make([]string, len(numStr))
	copy(digits, numStr)
	left := 0
	right := len(numStr) - 1
	for left < right {

		if digits[left] == digits[right] {
			left++
			right--
		} else {
			return false
		}
	}
	return true
}
func main() {
	resultOne := isPalindrome(121)
	fmt.Println(resultOne)
	resultTwo := isPalindrome(-121)
	fmt.Println(resultTwo)
	resultThree := isPalindrome(10)
	fmt.Println(resultThree)
}
