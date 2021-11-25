def maxArea(a):
    b = len(a)
    area = 0
    for i in range(b):
        for j in range(i+1, b):
            area = max(area, min(a[i],a[j])*(j-i))
    print(area)

def maxArea2(a):
    b = len(a)
    area = 0
    l = 0
    r = b-1

    while(l < r):
        area = max(area, min(a[l],a[r])*(r-l))
    
        if a[l]<a[r]:
            l += 1
        else:
            r -= 1
    
    print(area)

def main():
    list = [1,5,4,3]
    maxArea(list)
    maxArea2(list)


main()