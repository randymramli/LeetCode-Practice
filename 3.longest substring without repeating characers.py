def lengthOfLongestSubstring(s):
    a = len(s)

    ans = 0

    map = {}
        # s = "abcabcbb"

    i = 0
    for j in range(a):
        print(map)
        if s[j] in map:
            i = max(map[s[j]], i)
            print("i: ",i)
        
        ans = max(ans,j-i+1)
        print("ans: ", ans)
        map[s[j]] = j + 1

    print(ans)

def length2(s):
    map = {}
    max_length = 0
    start = -1

    for i, v in enumerate(s):
        if v in map and map[v] > start:
            start = map[v]
        elif i - start > max_length:
            max_length = i -start
        map[v] = i
    print(max_length)


if __name__ == '__main__':
    s = "abcabcbb"
    lengthOfLongestSubstring(s)
    length2(s)