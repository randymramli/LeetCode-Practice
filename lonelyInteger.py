def lonelyinteger(arr):
    # Write your code here
    # print(arr[[[arr1 ^ x for x in arr].count(0) for arr1 in arr].index(1)])
    
    haha = []
    for arr1 in arr:
        for x in arr:
            haha.append(arr1 ^ x)
    print(haha)
    
    hihi = haha.count(0)
    hihi = str(hihi)
    print(hihi.index(1))
    
    # return hihi.index(1)

if __name__ == '__main__':
    a = [1,2,3,4,3,2,1]
    lonelyinteger(a)