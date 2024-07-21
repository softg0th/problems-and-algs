package main

import (
	"fmt"
	"strings"
)

func ToCamelCase(s string) string {
	analyzeString := strings.Split(s, "")
	var newStringArr []string

	for i := 0; i < len(analyzeString); i++ {
		if string(analyzeString[i]) != "_" && string(analyzeString[i]) != "-" {
			newStringArr = append(newStringArr, analyzeString[i])
		} else {
			fmt.Println(i)
			newStringArr = append(newStringArr, strings.ToUpper(analyzeString[i+1]))
			i += 1
		}

	}
	res := strings.Join(newStringArr, "")
	return res
}

func main() {
	resultOne := ToCamelCase("the-stealth-warrior")
	fmt.Println(resultOne)
	resultTwo := ToCamelCase("The_Stealth_Warrior")
	fmt.Println(resultTwo)
	resultThree := ToCamelCase("The_Stealth-Warrior")
	fmt.Println(resultThree)
}
