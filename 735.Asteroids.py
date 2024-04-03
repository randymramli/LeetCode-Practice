def asteroidCollision(asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 > a:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                break
            else:
                stack.append(a)
        
        print(stack)

if __name__ == '__main__':
    s = [5,10,-5]
    a = [-2,-1,1,2]
    c = [2,-2,3,4,-3,1,-2,10]
    asteroidCollision(s)
    asteroidCollision(a)
    asteroidCollision(c)
