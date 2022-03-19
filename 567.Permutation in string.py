import collections

def checkInclusion(s1, s2):
    a = len(s1)
    b = len(s2)
    loop_range = b - a + 1

    s1_counter = collections.Counter(s1)

    for i in range(loop_range):
        c = s2[i:i+a]
        if collections.Counter(c) == s1_counter:
            return True
    return False



if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    checkInclusion(s1,s2)