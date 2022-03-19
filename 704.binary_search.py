def binary(list, target):
    l = 0
    r = len(list) -1
    while l <= r:
        mid = (l+r)//2
        if list[mid] == target:
            print(mid)
        if list[mid] < target:
            l = mid +1
        else:
            r = mid -1
    # if item not in list
    return -1

def binary_recursion(list, target, low, high):
    if 1 <= high:
        mid = low + (high - low)//2

        if list[mid] == target:
            print(mid)
        elif target < list[mid]:
            binary_recursion(list, target, low, mid-1)
        else:
            binary_recursion(list, target, mid, high)

def main():
    nums = [-1,0,3,5,9,12]
    target = 9
    #binary(nums, target)
    binary_recursion(nums, target, 0, len(nums) -1)


main()