package main

func maxDepth(s string) int {
	maxLen := 0
	commonLen := 0

	for _, character := range s {
		if string(character) == "(" {
			commonLen += 1
		} else if string(character) == ")" {
			if maxLen < commonLen {
				maxLen = commonLen
			}
			commonLen -= 1
		}
	}
	return maxLen
}
