class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head

        for i in range(index + 1):
            current = current.next
        
        return current.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        
        self.size += 1

        prev = self.head
        for i in range(index):
            prev = prev.next
        
        new_node = ListNode(val)

        new_node.next = prev.next
        prev.next = new_node


        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1

        prev = self.head

        for i in range(index):
            prev = prev.next
        
        prev.next = prev.next.next