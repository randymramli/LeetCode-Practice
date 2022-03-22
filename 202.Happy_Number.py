def isHappy(n):
    total = str(n)
    if len(str(n)) == 1 or len(str(n)) <= 0:
        print('false')
    else:
        while n != 1:
            new = 
            for i in len(str(n)):
                n += int(n) * int(n)
                print(n)
        print('true')


if __name__ == '__main__':
    num = 19
    isHappy(num)