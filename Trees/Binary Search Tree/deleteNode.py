#Binary search tree(deleting a node)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


    def deleteNode(self,node):
        if not self.root:
            print('No Tree exist')
        else:
            temp = self.root
            prev = temp
            right = False
            left = False
            while temp.val != node:
                prev = temp
                if temp.val > node:
                    right = False
                    left = True
                    temp = temp.left
                elif temp.val < node:
                    left = False
                    right = True
                    temp = temp.right
                if not temp:
                    break
            if not temp.right and not temp.left:
                if left:
                    prev.left = None
                elif right:
                    prev.right = None
            elif temp.right and not temp.left:
                if left:
                    prev.left = temp.right
                elif right:
                    prev.right = temp.right
            elif not temp.right and temp.left:
                if left:
                    prev.left = temp.left
                elif right:
                    prev.right = temp.left
            elif temp.right and temp.left:
                nextNode = temp.right
                prevNode = None
                while nextNode.left:
                    prevNode = nextNode
                    nextNode = nextNode.left
                value = nextNode.val
                if prevNode:
                    if nextNode.right:
                        prevNode.left = nextNode.right
                    else:
                        prevNode.left = None
                    temp.val = value
                else:
                    temp.val = value
                    temp.right = nextNode.right


def main():
    obj = BinaryTree()
    obj.deleteNode(19)


main()