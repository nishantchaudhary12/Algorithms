#stack using lists

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            self.items.pop()
        else:
            print('No stack')

    def display(self):
        if self.items:
            print(self.items)
        else:
            print('No stack')

    def top(self):
        if self.items:
            print(self.items[-1])
        else:
            print('No stack')

    def size(self):
        if self.items:
            print(len(self.items))
        else:
            print('No stack')

    def isEmpty(self):
        if self.items:
            print('False')
        else:
            print('True')


def main():
    obj = Stack()
    obj.isEmpty()
    obj.display()
    obj.pop()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.size()
    obj.display()
    obj.pop()
    obj.display()
    obj.pop()
    obj.size()
    obj.display()
    obj.top()
    obj.isEmpty()


main()
