def removeElement(nums, val):
    new_nums = []
    for i in nums:
        if val != nums[i]:
            new_nums.append(nums[i])
    
    print(new_nums)

def removeElement2(nums, val):
    abc = 0
    for i in range(len(nums)):
        if val != nums[i]:
            nums[abc] = nums[i]
            print(nums)
            abc+=1
    
    print(abc)



if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    removeElement2(nums,val)