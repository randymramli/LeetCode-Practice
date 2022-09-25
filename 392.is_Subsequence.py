def isSubsequence(s, t):
    left = right = 0
    left_len, right_len = len(s), len(t)

    while left < left_len and right < right_len:
        if s[left] == t[right]:
            left += 1
        right += 1
    
    return left == left_len
    

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    isSubsequence(s,t)