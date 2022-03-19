def sortedSquares(nums):
    b = len(nums)
    c = []
    for i in range(b):
        c.append(nums[i]**2)
    
    c.sort()

    print(c)

if __name__ == '__main__':
    a = [-4,-1,0,3,10]
    sortedSquares(a)