def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            print('False')
        
        newdict = {}
        
        for i in s:
            if i not in newdict:
                newdict[i] = 1
            else:
                newdict[i] += 1
        
        for j in t:
            if j not in newdict:
                print('False')
            else:
                newdict[j] -= 1
        
        for val in newdict.values():
            if val != 0:
                print('False')
        
        print('True')

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    isAnagram(s,t)
    a = "charlie"
    b = "chomhie"
    isAnagram(a,b)