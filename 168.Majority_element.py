def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thisdict = {}
        half = (len(nums) /2)
        result = []

        for num in nums:
            if num not in thisdict:
                thisdict[num] = 1
            else:
                thisdict[num] += 1
        for x,y in thisdict.items():
            if y > half:
                if len(result) == 0:
                    result.append(x)
                    result.append(y)
                    continue
                if y > result[1]:
                    result[0] = x
                    result[1] = y
        print(result)
            

if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    majorityElement(nums)