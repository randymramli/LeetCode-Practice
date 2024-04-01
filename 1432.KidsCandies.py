def kidsWithCandies(candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        highestNum = max(candies)
        kidNum = len(candies)
        result = []
        for i in range(kidNum) :
            print(candies[i] + extraCandies)
            if ((candies[i] + extraCandies) >= highestNum):
                result.append(True)
            else:
                result.append(False)
        print(highestNum)
        print(result)

if __name__ == '__main__':
     candies = [2,3,5,1,3]
     extra = 3
     kidsWithCandies(candies, extra)