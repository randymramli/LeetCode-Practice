def subsets(nums):
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        print(output)

def subsetsBitmask(nums):
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask

            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        print(output)

if __name__ == '__main__':
    nums = [1,2,3]
    # subsets(nums)
    subsetsBitmask(nums)