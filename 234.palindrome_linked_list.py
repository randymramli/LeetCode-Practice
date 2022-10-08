def isPalindrome(head):
    result = []
    while head.next is not None:
        result.append[head.val]
        head = head.next
    return result == result[::-1]