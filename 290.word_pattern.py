def wordPattern(pattern, s):
    patdict = {}

    a = s.split(" ")

    if len(pattern) != len(a) :
        print('false')
    
    for i in range(len(pattern)):
        if pattern[i] not in patdict:
            if a[i] in patdict.values():
                return False
            else:
                patdict[pattern[i]] = a[i]
        elif (pattern[i] in patdict) and (patdict[pattern[i]] != a[i]):
            print('false')
            return

    print('true')
        
if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat do"
    wordPattern(pattern,s)