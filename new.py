def twoSum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        #print(i)
        #print(num)
        n = target - num
        #print(n)
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]
    print(h)


def main() :
    nums = [3,2,4]
    point = 9
    twoSum(nums,point)

main()

# 3:0
# 2:1
# 4:2