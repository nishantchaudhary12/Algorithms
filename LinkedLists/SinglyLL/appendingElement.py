#singly linked list
#appending a new node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)

        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(val)


def main():
    my_list = LinkedList()
    my_list.append(2)
    my_list.append(4)
    my_list.append(6)


main()