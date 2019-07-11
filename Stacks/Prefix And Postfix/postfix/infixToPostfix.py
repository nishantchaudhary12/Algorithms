#infix to postfix conversion


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


def infix_postfix(user_ip):
    obj = Stack()
    postfix = list()
    my_dict = {1: ['**'], 2: ['/', '*'], 3: ['+', '-']}
    for each in user_ip:
        # obj.display()
        if not each.isalnum():
            top = obj.top()
            if top in my_dict[1] and each in my_dict[1]:
                postfix.append(obj.pop())
                obj.push(each)
            elif top in my_dict[2] and each in my_dict[2]:
                postfix.append(obj.pop())
                obj.push(each)
            elif top in my_dict[3] and each in my_dict[3]:
                postfix.append(obj.pop())
                obj.push(each)
            elif each == ')':
                curr = obj.pop()
                while curr != '(':
                    postfix.append(curr)
                    curr = obj.pop()
            elif each in my_dict[3] and (top in my_dict[1] or top in my_dict[2]):
                # postfix.append(obj.pop())
                if top in my_dict[1]:
                    postfix.append(obj.pop())
                    obj.push(each)
                if top in my_dict[2]:
                    postfix.append(obj.pop())
                    obj.push(each)
            elif each in my_dict[2] and top in my_dict[1]:
                postfix.append(obj.pop())
                obj.push()
                # if top in my_dict[1]:
                #     postfix.append(obj.pop())
                #     obj.push(each)
            else:
                obj.push(each)
        else:
            postfix.append(each)

    while not obj.isEmpty():
        postfix.append(obj.pop())
    # print('postfix', postfix)
    result = ''.join(postfix)
    print('Postfix:', result)
    return postfix


def main():
    # user_ip = '( 4 + 8 ) * ( 6 - 5 ) / ( ( 3 - 2 ) * ( 2 + 2 ) )'
    # user_ip = 'A+B/C*(D+E)-F'
    # user_ip = '3 + 4 * 5 / 6'
    user_ip = '( 300 + 23 ) * ( 43 - 21 ) / ( 84 + 7 )'
    user_ip_list = user_ip.split(' ')
    # print(user_ip_list)
    postfix = infix_postfix(user_ip_list)
    print(postfix)


if __name__ == '__main__':
    main()
