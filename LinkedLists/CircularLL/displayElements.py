#circular linked list
#display nodes of linked list


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
                if temp == self.head:
                    break


def main():
    my_list = LinkedList()
    my_list.display()


main()