from unittest import result


def runningSum(snums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(snums)
        result = []
        result.append(snums[0])
        for i in range(1,l):
            total = result[i-1] + snums[i]
            result.append(total)

if __name__ == '__main__':
    nums = [1,2,3,4]
    runningSum(nums)