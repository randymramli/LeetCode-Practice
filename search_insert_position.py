def searchInsert(numList, target):
    left = 0
    right = len(numList)-1
    while left <= right:
        mid = (left + right)//2
        if numList[mid] == target:
            return mid
        if target < numList[mid]:
            right = mid -1
        else:
            left = mid +1
    print(left)



if __name__ == '__main__':
    numList = [1,3,5,7]
    targetNum = 2
    searchInsert(numList,targetNum)