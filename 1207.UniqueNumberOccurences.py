def uniqueOccurrences(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashMap = {}
        for i in arr:
            if i in hashMap.keys():
                 hashMap[i] += 1
            else:
                 hashMap[i] = 1

        
        return len(list(set(hashMap.values()))) == len(hashMap.values())
        


if __name__ == '__main__':
    arr = [1,2,2,1,1,3]
    uniqueOccurrences(arr)