package main

import "sort"

func fillTheMap(realMap map[string]int, source string) map[string]int {
	for _, char := range source {
		_, ok := realMap[string(char)]
		if ok {
			realMap[string(char)] += 1
		} else {
			realMap[string(char)] = 1
		}
	}
	return realMap
}

func sortedKeysChecker(data map[string]int) []int {
	values := []int{}

	for _, value := range data {
		values = append(values, value)
	}

	sort.Slice(values, func(i, j int) bool {
		return values[i] < values[j]
	})

	return values
}

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}

	firstMap := make(map[string]int)
	secondMap := make(map[string]int)
	firstMap = fillTheMap(firstMap, word1)
	secondMap = fillTheMap(secondMap, word2)

	firstVals := sortedKeysChecker(firstMap)
	secVals := sortedKeysChecker(secondMap)

	for char, _ := range firstMap {
		_, ok := secondMap[char]

		if !ok {
			return false
		}
	}

	for i := range firstVals {
		if firstVals[i] != secVals[i] {
			return false
		}
	}
	return true
}
