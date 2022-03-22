def canMakeArithmeticProgression(arr):
    arr.sort()
    length = len(arr)
    res = arr[0] - arr[1]

    for i in range(1,length-1):
        if (arr[i] - arr[i+1]) == res:
            continue
        else:
            print("false")
            break
    print('true')


if __name__ == '__main__':
    arr = [3,5,1]
    arr2 = [1,2,4]
    arr3 = [-13,-17,-8,-10,-20,2,3,-19,2,-18,-5,7,-12,18,-17,12,-1]
    # canMakeArithmeticProgression(arr)
    # canMakeArithmeticProgression(arr2)
    canMakeArithmeticProgression(arr3)