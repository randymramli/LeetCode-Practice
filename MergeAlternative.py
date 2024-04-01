def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        count = 0
        len1 = len(word1)
        len2 = len(word2)
        res = ""
        if (len1 < len2):
            for i in range(len1):
                res = res + word1[i] + word2[i]
            res = res + word2[len1:]
        elif (len2 < len1):
            for i in range(len2):
                res = res + word1[i] + word2[i]
            res = res + word1[len2:]
        else:
            for i in range(len1):
                res = res + word1[i] + word2[i]

            
        print(res)

if __name__ == '__main__':
     word1 = "ab"
     word2 = "pqrs"
     mergeAlternately(word1, word2)