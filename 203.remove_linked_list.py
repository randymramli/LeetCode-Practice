class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(self, head, val):
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    
    while head:
        if head.val == val:
            prev.next = head.next
        else:
            prev = head
        head = head.next
    
    return dummy.next