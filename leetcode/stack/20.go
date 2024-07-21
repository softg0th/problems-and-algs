package internal

func IsValid(s string) bool {
	var brackets []string
	var bracketMap = map[string]string{
		"(": ")",
		"{": "}",
		"[": "]",
	}
	for j := 0; j < len(s); j++ {
		switch string(s[j]) {
		case "(", "{", "[":
			brackets = append(brackets, string(s[j]))
		case ")", "}", "]":
			if len(brackets) == 0 {
				return false
			}
			current := brackets[len(brackets)-1]
			brackets = brackets[:len(brackets)-1]
			if bracketMap[current] != string(s[j]) {
				return false
			}
		}
	}
	return len(brackets) == 0
}
