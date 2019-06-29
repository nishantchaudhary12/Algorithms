#circular linked list
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
            count = 1
            if num == 1:
                var = temp.next
                while temp:
                    prev = temp
                    # print(prev.val)
                    temp = temp.next
                    # print(temp.val)
                    if temp == self.head:
                        break
                self.head = var
                prev.next = self.head

            else:
                flag = True
                while num != count:
                    prev = temp
                    temp = temp.next
                    count += 1
                    if temp == self.head:
                        print('Invalid Index')
                        flag = False
                        break
                if flag:
                    prev.next = temp.next


def main():
    my_list = LinkedList()
    my_list.delete(3)


main()