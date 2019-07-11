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


def parenthesis(user_ip):
    obj = Stack()
    flag = False
    braces_dict = {'[': ']', '{': '}', '(': ')'}
    for each in user_ip:
        if each in ('[', '{', '('):
            obj.push(each)
        elif each in (']', '}', ')'):
            if not obj.isEmpty():
                curr = obj.pop()
                if braces_dict[curr] == each:
                    flag = True
                else:
                    flag = False
            else:
                flag = False
            if not flag:
                break
    if not obj.isEmpty():
        flag = False
    return flag


def main():
    user_ip = ['[', '(', ']', ')', '{', '}']
    print(parenthesis(user_ip))


if __name__ == '__main__':
    main()
