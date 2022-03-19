def maxSubArray(nums):
    current = nums[0]
    max_sub = nums[0]
    
    for i in nums[1:]:
        current = max(i, current + i)
        max_sub = max(max_sub, current)
    
    print(max_sub)

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    maxSubArray(nums)