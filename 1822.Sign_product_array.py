def arraySign(nums):
    result = 1
    for i in nums:
        result *= i

    if result == 0:
        return 0
    elif result > 0 :
        return 1
    else:
        return -1

if __name__ == '__main__':
    nums = [-1,-2,-3,-4,3,2,1]
    arraySign(nums)