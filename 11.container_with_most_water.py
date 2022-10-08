from bisect import bisect_right


def maxArea(height):
    b = len(height)
    area = 0
    l = 0
    r = b-1

    while(l < r):
        area = max(area, min(height[l],height[r])*(r-l))
        print(area)

        if height[l]<height[r]:
            l += 1
        else:
            r -= 1

    print(area)

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    maxArea(height)