def containsDuplicate(nums):
    new_dict = {}
    for i in nums:
        if i in new_dict:
            return True
        else:
            new_dict[i] = 1
    return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    containsDuplicate(nums)