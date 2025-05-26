def hammingWeight(n):
    print(bin(n)[2:])
    res = 0
    while n != 0:
        n &= (n-1)
        res += 1
    
    print(res)


if __name__ == '__main__':
    n = 125
    hammingWeight(n)