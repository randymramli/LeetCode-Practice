class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorderTraversal(root):
    result = []
    helperMethod(root, result)
    print(result)

def helperMethod(root, list):
    if root:
        if root.left:
            helperMethod(root.left, list)
        
        list.append(root.val)

        if root.right:
            helperMethod(root.right, list)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    inorderTraversal(root)