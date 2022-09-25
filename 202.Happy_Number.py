def isHappy(n):
    nums = set()
    while True:
      n = sum(int(c) ** 2 for c in str(n))
      if n == 1:
        print('true')
        return
      
      if n in nums:
        print('false')
        return False
      nums.add(n)

if __name__ == '__main__':
    num = 7
    isHappy(num)