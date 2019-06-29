#doubly linked list
#inserting a node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, num, val):
        if not self.head:
            print('No list exist')
        else:
            flag = True
            new = Node(val)
            temp = self.head
            if num == 1:
                self.head = new
                new.next = temp
            else:
                count = 1
                while True:
                    count += 1
                    if count == num:
                        break
                    temp = temp.next
                    if not temp or count > num:
                        print('Invalid Index')
                        flag = False
                        break
                if flag:
                    var = temp.next
                    temp.next = new
                    new.next = var


def main():
    my_list = LinkedList()
    my_list.insert(3, 12)


main()