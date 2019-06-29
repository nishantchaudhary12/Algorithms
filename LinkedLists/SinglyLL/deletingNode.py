#singly linked list
#deleting a node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete(self, num):
        if not self.head:
            print('No list exist')
        else:
            flag = True
            while count != num:
                prev = temp
                temp = temp.next
                count += 1
                if temp == None:
                    print('Wrong Index')
                    flag = False
                    break
            if flag:
                prev.next = temp.next


def main():
    my_list = LinkedList()
    my_list.delete(3)


main()