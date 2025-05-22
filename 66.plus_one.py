def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):

        if digits[i] + 1 != 10:
            digits[i] += 1
            print(digits)
            return digits
        
        digits[i] = 0

        if i == 0:
            return [1] + digits


if __name__ == '__main__':
    a = [1,2,4]
    b = [4,9,9]
    # plusOne(a)
    plusOne(b)