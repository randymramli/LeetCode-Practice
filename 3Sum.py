def threeSum(nums):
    a = len(nums)
    nums.sort()
    result = []
    for i in range(a):
        if nums[i] > 0:
            break
        if i == 0 or nums[i] != nums[i-1]:
            twoSum(nums, i, result)
    print(result)

def twoSum(nums, i, result):
    low = i + 1
    high = len(nums) -1
    while (low < high):
        sum = nums[i] + nums[low] + nums[high]
        if sum > 0:
            high -= 1
        elif sum < 0:
            low += 1
        else:
            result.append([nums[i], nums[low], nums[high]])
            low += 1
            high -= 1
            while low < high and nums[low] == nums[low -1]:
                low += 1

if __name__ == '__main__':
    list = [-1,0,1,2,-1,-4]
    threeSum(list)