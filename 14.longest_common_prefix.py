from signal import strsignal


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

def test(strs):
    answer = ""
    # result = zip(*strs)
    # for i in result:
    #     print(i)

    for i in zip(*strs):
        if len(set(i)) == 1:
            # print(set(i))
            answer += i[0]
            print(answer)
        else:
            break
    return answer

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    # longestCommonPrefix(strs)
    # a = zip(*strs)
    # for i in a:
    #     print(i)
    test(strs)