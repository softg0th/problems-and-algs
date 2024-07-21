package main

func maxProfit(prices []int) int {
	minprice := 999999999999999999
	maxprice := 0

	for i := range prices {
		if prices[i] < minprice {
			minprice = prices[i]
		} else if prices[i]-minprice > maxprice {
			maxprice = prices[i] - minprice
		}
	}
	return maxprice
}
