def maxProfit(prices):
    abc = len(prices)
    if len(prices) == 0:
        return 0
    else:
        maxprofit = 0
        for i in range(abc-1):
            for j in range(1,abc):
                profit = prices[j] - prices[i]
                if (profit > maxprofit):
                    maxprofit = profit
    
    print(maxprofit)




if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    maxProfit(prices)