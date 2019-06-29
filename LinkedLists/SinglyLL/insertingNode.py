#singly linked list
#inserting a node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def inserting(self, num, val):
        new = Node(val)
        if not self.head:
            print('No list exist')
        else:
            temp = self.head
            count = 1
            if num == 1:
                self.head = new
                new.next = temp
            else:
                flag = True
                while count != num:
                    prev = temp
                    temp = temp.next
                    count += 1
                    if count == num:
                        break
                    if temp == None:
                        print('Wrong Index')
                        flag = False
                        break
                if flag:
                    var = prev.next
                    prev.next = new
                    new.next = var


def main():
    my_list = LinkedList()
    my_list.inserting(3, 12)


main()