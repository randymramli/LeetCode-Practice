def strStr(haystack, needle):
    needlen = len(needle)
    haylen = len(haystack)
    range_stop = haylen - needlen + 1
    print(needlen)
    print(haylen)
    print(range_stop ,"\n")


    for i in range(0, range_stop):
        range_end = i + needlen
        # print(range_end)
        print(f"{i}: {haystack[i:range_end]}")
        if haystack[i:range_end] == needle:
            print(i)
            break
    
    print('-1')



if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    haystack2 = "leetcodeleemnagartyuleetolkjnafag"
    needle2 = "leeto"
    haystack3 = "hell"
    needle3 = "ll"
    # strStr(haystack,needle)
    strStr(haystack3,needle3)