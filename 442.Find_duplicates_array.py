def findDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for i in nums:
            i = abs(i)
            if nums[i-1] < 0:
                result.append(i)
            nums[i-1] *= -1

        print(result)

if __name__ == "__main__":
     nums = [4,3,2,7,8,2,3,1]
     findDuplicates(nums)