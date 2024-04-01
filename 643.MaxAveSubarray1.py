def findMaxAverage(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxVal = float('-inf')
        length = len(nums)
        print(length)

        if length < k:
            return False
        
        if length == k:
            return (sum(nums) / k)

        maxRange = length - k + 1

        for i in range(maxRange):
            # print(i)
            # print(nums[i:(i+k)])
            total = (sum(nums[i:(i+k)]))/k
            # print(total)
            maxVal = max(maxVal, total)
  
        
        print(maxVal)
    
def findMaxAverage2( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        movingSum = 0

        for x in range(0, k, 1):
            movingSum += nums[x]
        
        maxRes = movingSum

        for x in range(k, len(nums), 1):
            movingSum -= nums[x-k]
            movingSum += nums[x]
            if movingSum > maxRes:
                maxRes = movingSum

        return (maxRes/float(k))


if __name__ == '__main__':
    arr = [1,12,-5,-6,50,3]
    arr2 = [0,1,1,3,3]
    k = 4
    findMaxAverage(arr2, k)