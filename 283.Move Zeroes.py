def moveZeroes(nums):
    b = len(nums)
    i = 0
    counter = 0
    while counter < b:
        if nums[i] == 0:
            nums.append(nums.pop(i))
        else:
            i += 1
            counter += 1

def moveZeroesSecond(nums):
    index = 0

    for count, values in enumerate(nums):
        if values != 0:
            nums[index] = values
            if count != index:
                nums[count] = 0
            index += 1




if __name__ == '__main__':
    a = [0,1,0,3,12]
    moveZeroes(a)