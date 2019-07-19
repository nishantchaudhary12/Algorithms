#Binary search tree(searching a node)


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

    def searchNode(self, node):
        if not self.root:
            print('No Tree Exist')
        else:
            temp = self.root
            while temp.val != node:
                if temp.val > node:
                    temp = temp.left
                elif temp.val < node:
                    temp = temp.right
                if not temp:
                    break
            if temp:
                return temp
            else:
                return -1




def main():
    sample_input = [29, 34, 28, 38, 36, 19, 4, 32, 31, 25, 42, 41, 39, 2, 5, 10, 24, 40]
    obj = BinaryTree()
    for each in sample_input:
        obj.addNode(each)
    print(obj.searchNode(40))


main()