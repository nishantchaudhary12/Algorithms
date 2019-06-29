#circular linked list
#adding a node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
            new.next = self.head
        else:
            temp = self.head
            while temp:
                prev = temp
                temp = temp.next
                if temp == self.head:
                    break
            prev.next = new
            new.next = self.head


def main():
    my_list = LinkedList()
    my_list.append(2)
    my_list.append(4)
    my_list.append(6)
    my_list.append(8)
    my_list.append(10)


main()