#queue using lists
#linear queue


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def display(self):
        if self.items:
            print(self.items)
        else:
            print('Queue is empty')

    def size(self):
        if self.items:
            print(len(self.items))
        else:
            print('Queue is empty')

    def isEmpty(self):
        if not self.items:
            return True
        return False

    def front(self):
        if self.items:
            print(self.items[0])
        else:
            print('Queue is empty')


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


main()