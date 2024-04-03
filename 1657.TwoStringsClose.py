def closeStrings(word1, word2):
        if len(word1) != len(word2):
            return False
        dict1 = {}
        dict2 = {}

        for i in range(len(word1)):
            if word1[i] not in dict1:
                dict1[word1[i]] = 1
            else:
                dict1[word1[i]] += 1
        
        for i in range(len(word2)):
            if word2[i] not in dict2:
                dict2[word2[i]] = 1
            else:
                dict2[word2[i]] += 1
        
        
        if set(dict1.keys()) != set(dict2.keys()):
            return False

        ab = list(dict1.values())
        bc = list(dict2.values())

        ab.sort()
        bc.sort()

        return ab == bc


if __name__ == '__main__':
    word1 = "aaabbbbccddeeeeefffff"
    word2 = "aaaaabbcccdddeeeeffff"
    closeStrings(word1,word2)