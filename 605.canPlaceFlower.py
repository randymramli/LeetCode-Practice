def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        availableLot = 0
        first = 0
        secondLot = 1
        last = -1
        totalBed = len(flowerbed)

        # print(flowerbed)
        # print(totalBed)

        if (flowerbed[first] == 0 and flowerbed[first + 1] == 0):
            n -= 1
        if (flowerbed[last] == 0 and flowerbed[last - 1] == 0):
            n -= 1
        
        for i in range(secondLot, totalBed - 1):
            if (flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                print(flowerbed)
                n -= 1
        
        print(n)

        if n >= 1:
            print('false')
        else:
            print('true')
    
if __name__ == '__main__':
    lot = [1,0,0,0,1]
    n = 1
    canPlaceFlowers(lot, n)