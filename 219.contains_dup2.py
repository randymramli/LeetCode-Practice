def containsDuplicate(nums,k):
    a = len(nums)
    new_dict = {}
    for i in range(a):
        if nums[i] in new_dict and (abs(new_dict[nums[i]] - i)) <= k:
            return True
        new_dict[nums[i]] = i
    return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    k = 3
    containsDuplicate(nums, k)