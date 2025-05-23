def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    if len(strs) <= 1:
        return [strs]
    
    newdict = {}

    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in newdict:
            newdict[sorted_word] = [word]
        else:
            newdict[sorted_word].append(word)
    
    print(list(newdict.values()))

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    strs2 = ["a", "b", "ca", "ac"]
    groupAnagrams(strs2)