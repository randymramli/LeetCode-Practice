def isPalindrome(x):
    if x < 0:
        print("false")
    elif str(x) == str(x)[::-1]:
        print("true")
    else:
        print("false2")    
   

def main():
    num = 1234321
    num1 = 12345
    num2 = -12321
    isPalindrome(num)
    isPalindrome(num1)
    isPalindrome(num2)

main()