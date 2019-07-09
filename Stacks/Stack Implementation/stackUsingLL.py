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
            print('No stack exist')
        else:
            temp = self.head
            self.head = temp.next
            return temp.val

    def display(self):
        if not self.head:
            print('No stack exist')
        else:
            temp = self.head
            while (temp != None):
                print(temp.val)
                temp = temp.next

    def top(self):
        if not self.head:
            print('No stack exist')
        else:
            return self.head.val

    def isEmpty(self):
        if not self.head:
            print(True)
        else:
            print(False)

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

def main():
    obj = Stack()
    print('len', obj.length())
    obj.isEmpty()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print('len', obj.length())
    obj.display()
    print(obj.pop())
    obj.display()
    print(obj.top())
    obj.isEmpty()
    obj.length()


if __name__ == '__main__':
    main()
