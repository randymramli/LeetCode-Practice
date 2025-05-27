def maxSubArray(nums):
    curr_sum = 0
    maxResult = float('-inf')

    for i in range(len(nums)):
        curr_sum += nums[i]
        maxResult = max(maxResult, curr_sum)

        if curr_sum < 0:
            curr_sum = 0
    
    print(maxResult)


if __name__ == "__main__":
    a = [-2,1,-3,4,-1,2,1,-5,4]
    maxSubArray(a)