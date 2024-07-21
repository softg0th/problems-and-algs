package main

import "fmt"

type ListNode struct {
	data int
	next *ListNode
}

func reverseList(head *ListNode) []int {
	var reversedList []int
	var prev *ListNode
	curr := head
	for curr != nil {
		next := curr.next
		curr.next = prev
		prev = curr
		curr = next
	}
	for prev != nil {
		reversedList = append(reversedList, prev.data)
		prev = prev.next
	}
	return reversedList
}

func main() {
	node5 := &ListNode{5, nil}
	node4 := &ListNode{4, node5}
	node3 := &ListNode{3, node4}
	node2 := &ListNode{2, node3}
	node1 := &ListNode{1, node2}
	resultOne := reverseList(node1)
	fmt.Println(resultOne)
}
