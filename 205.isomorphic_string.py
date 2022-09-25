def isIsomorphic(s, t):
    map1 = {}
    
    for index, char in enumerate(s):
        if char not in map1:
            if t[index] in map1.values():
                return False
            else:
                map1[char] = t[index]
        else:
            if map1[char] != t[index]:
                return False
    
    return True




if __name__ == '__main__':
    s = "egg"
    t = "add"
    isIsomorphic(s,t)