#circular linked list
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
            print("No list exist")
        else:
            new = Node(val)
            var = self.head
            temp = self.head
            if num == 1:
                self.head = new
                print(self.head)
                new.next = temp
                print(new.next)
                while temp:
                    prev = temp
                    temp = temp.next
                    if temp == var:
                        break
                prev.next = self.head

            else:
                flag = True
                count = 1
                while count != num:
                    prev = temp
                    temp = temp.next
                    count += 1
                    if count == num:
                        break
                    if temp == self.head:
                        print('Invalid Index')
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