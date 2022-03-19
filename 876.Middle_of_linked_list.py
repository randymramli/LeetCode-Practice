# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def middleNode(head):
    # two pointers method

    run1 = head
    run2 = head
    while run2 and run2.next:
        run1 = run1.next
        run2 = run2.next.next
    return run1
    