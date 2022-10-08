def searchRange(nums, target):
    if len(nums) == 0:
        print([-1,-1])
    n, i, j = len(nums), -1, -1
    l, r = 0, n-1

    while l < r:
        mid = l + (r-l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid
        else:
            i, j = mid, mid
            while i - 1 >= 0 and nums[i-1] == target:
                i -= 1
            while j + 1 < n and nums[j+1] == target:
                j += 1
            break
    print(i,j)

if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    searchRange(nums, target)