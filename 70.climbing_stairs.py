def climbStairs(n):
    if n <= 3:
        return n
        
    a = int(3)
    b = int(2)
    
    while(n-3 > 0):
        a = a + b
        b = a - b
        n -= 1
    print(a)
if __name__ == '__main__':
    n = 5
    climbStairs(n)