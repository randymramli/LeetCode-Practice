def reverseBits(n):
    n = int(n)

    for i in range(8):
        res = (res << 1)
    
    print(res)

if __name__ == '__main__':
    n = "00000010100101000001111010011100"
    reverseBits(n)