def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        print(nums)
        result = nums.sort()

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    findKthLargest(nums, k)