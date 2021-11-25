def longestCommonPrefix(strs):
    a = len(strs)
    result = ""
    if strs is None or a == 0:
        print(result)
    
    if a == 1:
        print(strs)
    
    minlength = len(min((word for word in strs if word), key=len))

    for i in range(0, minlength):

        current = strs[0][i]

        for j in range(a):
            if strs[j][i] != current:
                return result
        result += current
    return result

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    longestCommonPrefix(strs)