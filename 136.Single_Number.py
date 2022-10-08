def singleNumber(nums):
    bit = 0

    for i in nums:
        bit ^= i
    print(bit)

if __name__ == '__main__':
    nums = [2,2,1,1,4,5,4,6,5]
    singleNumber(nums)