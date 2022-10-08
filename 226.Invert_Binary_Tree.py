def invertTree(root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        right = invertTree(root.right)
        left = invertTree(root.left)
        root.left = right
        root.right = left
        return root