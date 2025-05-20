def countOdds(low, high):
    low_res = low % 2
    high_res = high % 2

    if low_res == 0 and high_res == 0:
        print((high - low)//2)
    elif low_res != 0 and high_res != 0:
        print(((high - low)//2) + 1)
    else:
        print((high + 1 - low)//2)


if __name__ == '__main__':
    low = 3
    high = 7
    countOdds(low,high)