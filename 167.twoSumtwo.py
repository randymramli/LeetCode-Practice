def twoSum(numbers, target):
    a = len(numbers)
    for i in range(a):
        for j in range(i+1,a):
            if (numbers[i] + numbers[j]) == target:
                print(i+1)
                print(j+1)


def twoPointers(numbers, target):
    low = 0
    high = len(numbers) -1
    while low < high:
        result = numbers[low] + numbers[high]
        if result > target:
            high -= 1
        elif result < target:
            low +=1
        else:
            print(low+1)
            print(high+1)

if __name__ == '__main__':
    list = [2,7,11,15]
    target = 9
    twoSum(list,target)
    twoPointers(list,target)