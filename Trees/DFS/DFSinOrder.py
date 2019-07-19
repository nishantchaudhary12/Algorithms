#DFS InOrder


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
                print(temp.val.val)
                temp = temp.next

    def top(self):
        if not self.head:
            return -1
        else:
            print('top', self.head.val)
            return self.head.val

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False

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

    def displayDFSinOrder(self):
        if not self.root:
            print('No Tree')
        else:
            temp = self.root
            elem_list = list()
            obj = Stack()
            while True:
                while temp:
                    obj.push(temp)
                    temp = temp.left
                if not temp and not obj.isEmpty():
                    temp = obj.pop()
                    elem_list.append(temp.val)
                    temp = temp.right
                if not temp and obj.isEmpty():
                    break
            return elem_list


def main():
    sample_input = [29, 34, 28, 38, 36, 19, 4, 32, 31, 25, 42, 41, 39, 2, 5, 10, 24, 40, 40]
    obj = BinaryTree()
    for each in sample_input:
        obj.addNode(each)
    print(obj.displayDFSinOrder())


main()