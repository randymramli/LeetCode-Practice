def romanToInt(s):

    
    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    number=0

    last = len(s)-1

    for i in range(last):
        if (roman[s[i]] < roman[s[i+1]]):
            number -= roman[s[i]]
        else:
            number += roman[s[i]]
    
    number = number + roman[s[-1]]
    
    print(number)

if __name__ == '__main__':
    a = 'III'
    b = 'IV'
    romanToInt(a)
    romanToInt(b)