def rotate(nums, k):
    b = len(nums)
    c = [0] * b

    for i in range(b):
        c[(i+k) % b] = nums[i]
    
    nums[:] = c


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    k = 3
    rotate(a,k)