def subsets(nums):
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        print(output)

def subsets2(nums):
        output = [[]]

        for num in nums:
            temp_subset = []
            for curr in output:
                temp_subset += [curr + [num]]
            output = output + temp_subset

        # print(output)

def subsetsBitmask(nums):
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask

            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        print(output)

def backtrack(nums):
    n = len(nums)
    res, sol = [], []

    def abc(i):
        if i == n:
            res.append(sol[:])
            return
            
        abc(i+1)

        sol.append(nums[i])
        abc(i+1)
        sol.pop()
    
    abc(0)

    print(res)
    

if __name__ == '__main__':
    nums = [1,2,3]
    # subsets(nums)
    # subsetsBitmask(nums)
    # subsets2(nums)
    backtrack(nums)