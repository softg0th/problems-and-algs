package main

func findTheWinner(n int, k int) int {
	person := 0

	for i := 2; i <= n; i++ {
		person = (person + k) % i
	}
	return person + 1
}
