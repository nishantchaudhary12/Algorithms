#queue using linked lists
#circular queue


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.items = None

    def enqueue(self, item):
        if not self.items:
            self.items = Node(item)
        else:
            temp = self.items
            self.items = Node(item)
            self.items.next = temp

    def dequeue(self):
        if not self.items:
            return -1
        else:
            temp = self.items
            while temp.next:
                prev = temp
                temp = temp.next
            prev.next = None
            return temp.val

    def display(self):
        if not self.items:
            print('Queue is empty')
        else:
            temp = self.items
            while temp:
                print(temp.val)
                temp = temp.next

    def size(self):
        if not self.items:
            print(0)
        else:
            temp = self.items
            count = 1
            while temp.next:
                temp = temp.next
                count += 1
            print(count)

    def isEmpty(self):
        if not self.items:
            return True
        return False

    def front(self):
        if not self.items:
            print('Queue is empty')
        else:
            print(self.items.val)


def main():
    obj = Queue()
    print(obj.isEmpty())
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.display()
    print(obj.dequeue())
    obj.size()
    print(obj.isEmpty())
    obj.front()
    obj.display()
    print(obj.dequeue())


main()