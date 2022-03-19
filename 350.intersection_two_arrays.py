def intersect(nums1, nums2):
    if len(nums1) > len(nums2):
        result(nums1,nums2)
    else:
        result(nums2,nums1)

def result(num1,num2):
    map= {}

    for i in num2:
        if i not in map:
            map[i] = 0
        map[i] += 1
    
    ans = []

    for j in num1:
        count = map.get(j,0)
        if count > 0:
            ans.append(j)
            map[j] -= 1
    
    print(ans)


if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    intersect(nums1,nums2)