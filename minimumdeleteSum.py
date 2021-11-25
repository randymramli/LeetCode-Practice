def minimumDeleteSum(s1,s2):
    two_sum = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
    if not s1 or not s2: return two_sum

    dp = [[0] * len(s2) for _ in range(len(s1))]
    dp[0][0] = ord(s1[0]) if s1[0] == s2[0] else 0

    for i in range(1, len(s1)):
        dp[i][0] = max(dp[i - 1][0], ord(s1[i])) if s1[i] == s2[0] else dp[i - 1][0]
        print(dp)
    for j in range(1, len(s2)):
        dp[0][j] = max(dp[0][j - 1], ord(s2[j])) if s1[0] == s2[j] else dp[0][j - 1]
        print(dp)

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + ord(s1[i])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    '''
    print(dp)
    print(two_sum)
    print(dp[-1][-1])
    print(dp[-1][-1] << 1)
    #return two_sum - (dp[-1][-1] << 1)
    '''
    print(sum(ord(c) for c in s2))
    print(dp[-1][-1])



if __name__ == '__main__':
    str1 = "girrafe"
    str2 = "girfe"
    minimumDeleteSum(str1,str2)