def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res = 0
        for i in nums:
            if i != val:
                nums[res] = i
                res += 1
                print(res)
                print(nums)
        
        print(res)
        print(nums)

if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    removeElement(nums, val)