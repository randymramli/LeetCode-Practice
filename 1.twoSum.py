def twoSum(nums, target):
    array = []
    for i in range(len(nums)):
            for j in range(len(nums)):
                    if (nums[i]+nums[j] == target):
                        array.append(i)
                        array.append(j)
    # print(array)

def twoHash(nums, target):
    hashmap = {}
    a = len(nums)
    new = []
    for i in range(a):
        hashmap[nums[i]] = i
    print(hashmap)
    for i in range(a):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]
    print('[]')

def twoHashTwo(nums, target):
    hashmap = {}
    a = len(nums)
    for i in range(a):
        complement = target - nums[i]
        if complement in hashmap:
            print(i)
            print(hashmap[complement])
        hashmap[nums[i]] = i
            
if __name__ == '__main__':
    list = [2,3,6,11,7,15]
    target = 9
    # twoSum(list, target)
    # twoHash(list, target)
    # twoHashTwo(list, target)