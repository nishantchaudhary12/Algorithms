#postfix to prefix


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        if not self.head:
            self.head = Node(val)

        else:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp

    def pop(self):
        if not self.head:
            return -1
        else:
            temp = self.head
            self.head = temp.next
            return temp.val

    def display(self):
        if not self.head:
            print('No stack exist')
        else:
            my_list = list()
            temp = self.head
            while (temp != None):
                my_list.append(temp.val)
                temp = temp.next
            print(my_list)

    def top(self):
        if not self.head:
            return -1
        else:
            return self.head.val

    def isEmpty(self):
        flag = False
        if not self.head:
            flag = True
        return flag

    def length(self):
        if not self.head:
            return 0
        else:
            temp = self.head
            count = 1
            while temp:
                temp = temp.next
                count += 1
            return count


def postfixToPrefix(postfix):
    obj = Stack()
    for each in postfix:
        if each.isalnum():
            obj.push(each)
        else:
            opr1 = obj.pop()
            opr2 = obj.pop()
            curr = each + ' ' + opr2 + ' ' + opr1
            obj.push(curr)
    print(obj.pop())


def main():
    postfix = ['300', '23', '+', '43', '21', '-', '*', '84', '7', '+', '/']
    postfixToPrefix(postfix)
    # '/ * + 300 23 - 43 21 + 84 7'

main()