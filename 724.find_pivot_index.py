def pivotIndex(nums):
    length = len(nums)
    for i in range(length):
        left = sum(nums[0:i])
        right = sum(nums[i+1:length])
        if left == right:
            print(i)
    else:
        print('-1')

if __name__ == '__main__':
   nums = [1,7,3,6,5,6]
   pivotIndex(nums)