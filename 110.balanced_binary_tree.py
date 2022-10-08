def isBalanced(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        def dfs(root):
            if not root:
                return 0
            l = 1 + dfs(root.left)
            r = 1 + dfs(root.right)
            
            if abs(l - r) > 1:
                self.ans = False
                
            return max(l,r)
            
        
        self.ans = True
        dfs(root)
        return self.ans