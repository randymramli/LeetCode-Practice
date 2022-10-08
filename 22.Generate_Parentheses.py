def generateParenthesis(n):
        ans = []

        def dfs(l,r,s):
          if l == 0 and r == 0:
            print('c')
            print(ans)
            ans.append(s)
          if l > 0:
            print('a')
            print(l)
            print(ans)
            dfs(l - 1, r, s + '(')
          if l < r:
            print('b')
            print(r)
            print(ans)
            dfs(l, r - 1, s + ')')

        dfs(n, n, '')
        return ans

if __name__ == '__main__':
    n = 3
    generateParenthesis(n)