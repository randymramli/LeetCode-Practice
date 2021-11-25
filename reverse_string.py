def reverseString(input):
    left = 0
    right = len(input) -1
    while (left < right) :
        input[left], input[right] = input[right], input[left]
        left +=1
        right -=1
    print(input)

if __name__ == '__main__':
    input = ["h","e","l","l","o"]
    reverseString(input)