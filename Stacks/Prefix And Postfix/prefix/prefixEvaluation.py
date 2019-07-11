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


def postfix_evaluation(user_ip):
    obj = Stack()
    for each in user_ip:
        # print(each)
        if each.isdigit():
            obj.push(each)
            # obj.display()
        else:
            operator = each
            op_1 = float(obj.pop())
            op_2 = float(obj.pop())
            if operator == '**':
                curr = op_1 ** op_2
            elif operator == '/':
                curr = op_1 / op_2
            elif operator == '*':
                curr = op_2 * op_1
            elif operator == '+':
                curr = op_1 + op_2
            elif operator == '-':
                curr = op_1 - op_2
            obj.push(curr)
            # obj.display()
    return obj.pop()




def main():
    postfix = ['7', '84', '+', '21', '43', '-', '/', '23', '300', '+', '*']
    print(postfix_evaluation(postfix))


if __name__ == '__main__':
    main()
