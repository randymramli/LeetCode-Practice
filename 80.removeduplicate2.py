def removeDuplicates(nums):
    k = min(2, len(nums))

    for i in range(2,len(nums)):
        if nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k += 1
    
    print(k)


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    removeDuplicates(nums)