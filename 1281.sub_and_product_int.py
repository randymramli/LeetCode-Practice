def subtractProductAndSum(n):
    n = str(n)

    prod = 1
    sub = 0

    for i in n:
        prod *= int(i)
        sub += int(i)
    
    return (prod-sub)


if __name__ == '__main__':
    subtractProductAndSum(234)