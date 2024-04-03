def removeStars(s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        lenS = len(s)

        for i in range(lenS -1, -1, -1):
            if not result:
                result.append(s[i])
            elif (result[-1] == "*") and (s[i] != "*"):
                result.pop()
            else:
                result.append(s[i])
        result = "".join(result)
        print(result[::-1])

if __name__ == '__main__':
    s = "leet**cod*e"
    removeStars(s)