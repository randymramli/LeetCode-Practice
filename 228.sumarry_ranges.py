def summaryRanges(nums):
    res = []
    start = 0

    for i in range(len(nums)):
        print("i: ", i)
        print("s: ", start)
        if ((i+1) < len(nums)) and nums[i+1] == nums[i] + 1:
            print("\n")
            continue
        
        if start == i:
            a = nums[start]
            res.append(f"{a}")
            print("a first: ",a)
        else:
            a = f"{nums[start]} -> {nums[i]}"
            res.append(f"{a}")
            print("a last: ",a)
        
        start = i + 1
        print("\n")

    print(res)


if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    summaryRanges(nums)