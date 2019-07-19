#BFS


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.items = None
        self.head = None

    def enqueue(self, item):
        if not self.items:
            self.items = Node(item)
            self.head = self.items
        else:
            temp = self.items
            self.items = Node(item)
            self.items.next = temp
            temp.prev = self.items
            while temp:
                self.head = temp
                temp = temp.next

    def dequeue(self):
        if not self.items:
            return -1
        else:
            temp = self.head
            prev = temp.prev
            if not prev:
                self.items = None
                self.head = None
            else:
                prev.next = None
                self.head = prev
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
        if not self.head:
            print('Queue is empty')
        else:
            print(self.head.val)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def _add(self, val, temp):
        if val > temp.val:
            if temp.right:
                temp = temp.right
            else:
                return 0
        elif val < temp.val:
            if temp.left:
                temp = temp.left
            else:
                return 0
        return temp

    def addNode(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            temp = self.root
            while True:
                prev = temp
                if val == prev.val:
                    break
                temp = self._add(val, temp)
                if not temp:
                    if val > prev.val:
                        prev.right = TreeNode(val)
                        break
                    elif val < prev.val:
                        prev.left = TreeNode(val)
                        break

    def displayBFS(self):
        if not self.root:
            print('No Tree')
        else:
            temp = self.root
            elem_list = list()
            obj = Queue()
            # print(temp.val)
            # print(temp.left)
            # print(temp.right)
            obj.enqueue(temp)
            # print(temp.val)
            while temp:
                if not obj.isEmpty():
                    temp = obj.dequeue()
                    elem_list.append(temp.val)
                    if temp.left:
                        obj.enqueue(temp.left)
                    if temp.right:
                        obj.enqueue(temp.right)
                    if obj.isEmpty():
                        break
                else:
                    break
            return elem_list


def main():
    sample_input = [29, 34, 28, 38, 36, 19, 4, 32, 31, 25, 42, 41, 39, 2, 5, 10, 24, 40, 40]
    obj = BinaryTree()
    for each in sample_input:
        obj.addNode(each)
    print(obj.displayBFS())


main()