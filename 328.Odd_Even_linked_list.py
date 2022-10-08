def oddEvenList(head):
    new = head
    even = head.next
    even_head = even

    while(even != None and even.next != None) :
        new.next = even.next
        new = new.next
        even.next = new.next
        even = even.next
    new.next = even_head
    return head