package main

import (
	"strings"
)

func removeDuplicates(s string) string {
	var stack []string
	stackLen := 0

	for _, character := range s {
		if stackLen <= 0 {
			stack = append(stack, string(character))
			stackLen += 1
		} else if stack[stackLen-1] != string(character) {
			stack = append(stack, string(character))
			stackLen += 1
		} else {
			stack = stack[:stackLen-1]
			stackLen -= 1
		}
	}
	return strings.Join(stack, "")
}
