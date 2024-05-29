package main

import "fmt"

func romanToInt(s string) int {
	romanMap := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	weirdPairsMap := map[string]int{
		"IV": 4,
		"IX": 9,
		"XL": 40,
		"XC": 90,
		"CD": 400,
		"CM": 900,
	}
	var nums []int

	for i := 0; i < len(s); i++ {
		if s[i] == 'I' && i+1 < len(s) && (s[i+1] == 'V' || s[i+1] == 'X') {
			sum := string(s[i]) + string(s[i+1])
			if value, ok := weirdPairsMap[sum]; ok {
				nums = append(nums, value)
				i++
			}
		} else if s[i] == 'X' && i+1 < len(s) && (s[i+1] == 'L' || s[i+1] == 'C') {
			sum := string(s[i]) + string(s[i+1])
			if value, ok := weirdPairsMap[sum]; ok {
				nums = append(nums, value)
				i++
			}
		} else if s[i] == 'C' && i+1 < len(s) && (s[i+1] == 'D' || s[i+1] == 'M') {
			sum := string(s[i]) + string(s[i+1])
			if value, ok := weirdPairsMap[sum]; ok {
				nums = append(nums, value)
				i++
			}
		} else {
			nums = append(nums, romanMap[rune(s[i])])
		}
	}

	calcSum := 0

	for j := 0; j < len(nums); j++ {
		calcSum += nums[j]
	}

	return calcSum
}

func main() {
	resultOne := romanToInt("III")
	fmt.Println(resultOne)
	resultTwo := romanToInt("LVIII")
	fmt.Println(resultTwo)
	resultThree := romanToInt("MCMXCIV")
	fmt.Println(resultThree)
}
