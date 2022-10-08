def isPalindrome(s):
    result = (''.join(char for char in s if char.isalnum())).lower()
    print(result)

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    isPalindrome(s)