from collections import Counter

def commonCharacterCount(s1, s2):
    print(Counter(s1))
    print(Counter(s2))

    print(Counter(s1) & Counter(s2))

    common_letters = dict(Counter(s1) & Counter(s2)) 
    # print(common_letters)
    common_counts = list(common_letters.values())

    print(common_counts)

    result = sum(common_counts)

    return result

s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1,s2))