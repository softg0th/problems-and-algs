package main

import (
	"fmt"
	"strings"
)

func removeStars(s string) string {
	stack := []string{}
	stackLen := 0

	for _, char := range s {
		chr := string(char)

		if chr != "*" {
			stack = append(stack, chr)
			stackLen += 1
		} else {
			if stackLen > 0 {
				stackLen -= 1
				stack = stack[:stackLen]
			}
		}
	}
	return strings.Join(stack, "")
}