#doubly linked list
#appending a node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp


def main():
    my_list = LinkedList()
    my_list.append(2)
    my_list.append(4)
    my_list.append(6)
    my_list.append(8)
    my_list.append(10)


main()