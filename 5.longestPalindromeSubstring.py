def longestPalindrome(s: str) -> str:

        if s==s[::-1]: 
            return s
        left = longestPalindrome(s[1:])
        right = longestPalindrome(s[:-1])
        print(left)
        print(right)

        if len(left)>len(right):
            return left
        else:
            return right

if __name__ == '__main__':
     s = "babad"
     longestPalindrome(s)