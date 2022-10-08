def isSameTree(p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return isSameTree(p.right,q.right) and isSameTree(p.left,q.left)