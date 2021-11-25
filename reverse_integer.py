def reverse(x):
    if x == 0 :
        return 0;

    new = int(('-' if x < 0 else '') + str(abs(x))[::-1].lstrip("0"))

    if abs(new) > 2**31-1:
        return 0
    
    print(new)

def main():
    numbers = 2345
    numbers1 = -34567
    numbers2 = 234560
    reverse(numbers)
    reverse(numbers1)
    reverse(numbers2)

main()