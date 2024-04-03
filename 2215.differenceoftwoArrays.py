def findDifference(nums1, nums2):
    first = list(set(nums1) - set(nums2))
    second = list(set(nums2) - set(nums1))
    print(first, second)


if __name__ == '__main__':
    num1 = [1,2,3]
    num2 = [2,4,6]
    findDifference(num1, num2)