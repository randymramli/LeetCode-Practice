def getIntersectionNode(headA, headB):
    new_set = set()

    while headA is not None:
        new_set.add(headA)
        headA = headA.next
    
    while headB is not None:
        if headB in new_set:
            return headB
        headB = headB.next
    
    return None