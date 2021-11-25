class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    new_list = LinkedList()
    new_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    new_list.head.next = second;
    second.next = third;
    new_list.print()
