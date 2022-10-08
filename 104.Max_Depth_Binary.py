def maxDepth(root):
    if root is None:
        return 0
    if not root.left and not root.right:
        return 1
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1


if __name__ == '__main__':
    root = [3,9,20,null,null,15,7]
    maxDepth(root)