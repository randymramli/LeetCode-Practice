def maxProductSubarray(sub):
    maxProduct = 0
    left = 1
    right = 1

    length = len(sub)

    for i in range(length):
        if left == 0:
            left = 1
        if right == 0:
            right = 1
    
        left *= sub[i]
        print("left= ",left)
        j = length - i - 1
        right *= sub[j]
        print("right= ", right)

        maxProduct = max(left, right, maxProduct)
        print(maxProduct, "\n")
    
    print(maxProduct)

if __name__ == "__main__":
    rr = [-2, 6, -3, -10, 0, 2, 7, 0, 8]
    maxProductSubarray(rr)