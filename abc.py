from curses.ascii import isalnum


def solution(s, t):
    n = len(s)
    total = 0
    numbers = [0,1,2,3,4,5,6,7,8,9]
    if (n==1):
        return 1
    for i in range(n):
        if i in numbers:
            if (i == 0):
                result = s[i:] < t
                print(s[1:])
                print(result)
                if result:
                    total += 1
            elif (i == n-1):
                result = s[:i] < t
                print(result)
                if result:
                    total += 1
            else:
                new = s[:i] + s[i+1:]
                print(new)
                result = new < t
                print(result)
                if result:
                    total += 1
    print(total)

if __name__ == '__main__':
    s = 'ab12c'
    t = "1zz456"
    solution(s,t)