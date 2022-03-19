def maxProfit(prices):
    abc = len(prices)
    if len(prices) == 0:
        return 0
    else:
        maxprofit = 0
        for i in range(abc-1):
            for j in range(i+1,abc):
                profit = prices[j] - prices[i]
                if (profit > maxprofit):
                    maxprofit = profit
    
    print(maxprofit)

def maxProfit2(prices):
    minProfit = 8000
    maxProfit = 0
    a = len(prices)

    for i in range(a):
        if (prices[i] < minProfit):
            minProfit = prices[i]
        elif (prices[i] - minProfit > maxProfit):
            maxProfit = prices[i] - minProfit
    print(maxProfit)




if __name__ == '__main__':
    prices = [7,6,4,3,1,5]
    maxProfit(prices)
    maxProfit2(prices)