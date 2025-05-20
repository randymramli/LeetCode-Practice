def isPalindrome(s):
    # result = (''.join(char for char in s if char.isalnum())).lower()
    # print(result)

    res = ""

    for char in s:
        if char.isalnum():
            res += char.lower()
    
    abc = res[::-1] + "..abc"
    
    print(res)
    print(abc)


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    isPalindrome(s)