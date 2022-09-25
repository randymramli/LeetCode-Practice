import collections

def checkInclusion(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    if len_s1 > len_s2:
        return False
    
    s1_count = Counter(s1)
    s2_count = Counter()
    
    for i in range(len_s2):
        
        # add letters on the right side window
        s2_count[s2[i]] += 1
        
        # remove letters on the left side window
        
        if i >= len_s1:
            if s2_count[s2[i-len_s1]] == 1:
                del s2_count[s2[i-len_s1]]
            else:
                s2_count[s2[i-len_s1]] -= 1
                
        if s1_count == s2_count:
            return True
    
    return False



if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    checkInclusion(s1,s2)