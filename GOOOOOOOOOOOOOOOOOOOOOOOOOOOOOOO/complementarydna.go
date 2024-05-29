package main

import (
	"fmt"
	"strings"
)

func DNAStrand(dna string) string {
	dnaMap := map[string]string{
		"A": "T",
		"T": "A",
		"G": "C",
		"C": "G",
	}

	result := make([]string, len(dna))

	for i := 0; i < len(dna); i++ {
		result[i] = dnaMap[string(dna[i])]
	}

	res := strings.Join(result, "")
	return res
}

func main() {
	result := DNAStrand("ATTGC")
	fmt.Println(result)
}
