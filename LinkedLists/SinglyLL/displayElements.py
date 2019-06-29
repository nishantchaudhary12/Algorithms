#singly linked list
#display contents of a linked list


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print('No list exist')
        else:
            temp = self.head
            while(temp != None):
                print(temp.val)
                temp = temp.next


def main():
    my_list = LinkedList()
    my_list.display()


main()