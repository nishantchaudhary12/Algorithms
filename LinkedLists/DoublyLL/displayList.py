#doubly linked list
#displaying a list


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None


    def display(self):
        if not self.head:
            print('No list exist')
        else:
            temp = self.head
            while temp:
                print(temp.val)
                temp = temp.next



def main():
    my_list = LinkedList()
    my_list.display()


main()