def canConstruct(ransomNote, magazine):

    magz_dict = {}

    for i in magazine:
        if i not in magz_dict:
            magz_dict[i] = 1
        else:
            magz_dict[i] += 1
    
    for j in ransomNote:
        if j in magz_dict and magz_dict[j] > 0:
            magz_dict[j] -= 1
        else:
            print("False")
            return
    
    print("True")



if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "acab"
    canConstruct(ransomNote, magazine)
    