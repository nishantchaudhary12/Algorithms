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
            temp = self.head
            if num == 1:
                self.head = temp.next
            else:
                flag = True
                count = 1
                while count != num:
                    prev = temp
                    temp = temp.next
                    count += 1
                    if not temp or count > num:
                        print('Invalid Index')
                        flag = False
                        break
                if flag:
                    prev.next = temp.next


def main():
    my_list = LinkedList()
    my_list.delete(3)


main()