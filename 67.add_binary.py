def addBinary(a, b):
    c = bin(int(a, 2) + int(b, 2))[2:]

    d = int(a,2)
    e = int(b,2)
    f = bin(int(a, 2) + int(b, 2))
    print(d,e,f)

if __name__ == '__main__':
    a = '1010'
    b = '0011'
    addBinary(a,b)