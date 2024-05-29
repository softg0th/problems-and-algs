package main

import "fmt"

func isSubsequence(s string, t string) bool {
	tLen := len(t) - 1
	sLen := len(s)
	tStart := 0
	sStart := 0
	flag := 0

	if sLen == 0 {
		return true
	}

	for tStart <= tLen {
		if t[tStart] == s[sStart] {
			sStart += 1
			flag += 1
		}
		if flag == sLen {
			return true
		}
		tStart += 1
	}
	return false
}

func main() {
	pattern := "abc"
	template := "ahbgdc"

	isIt := isSubsequence(template, pattern)
	fmt.Println(isIt)
}
