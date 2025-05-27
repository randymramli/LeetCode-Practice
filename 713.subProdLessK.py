def solution(array, k):
    res = 0
    l = 0
    ln = len(array)
    product = 1

    for i in range(ln):
        product *= array[i]
        while l <= i and product >= k:
            product //= array[l]
            l += 1
        res += (i - l + 1)

    print(res)

if __name__ == "__main__":
    rr = [1, 9, 2, 8, 6, 4, 3] 
    k = 100
    solution(rr,k)