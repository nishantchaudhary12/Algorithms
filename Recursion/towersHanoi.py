#towers of Hanoi


def hanoi(n, left, right, center):
    if n == 1:
        curr = left.pop()
        right.append(curr)
    else:
        hanoi(n-1, left, center, right)
        curr = left.pop()
        right.append(curr)
        hanoi(n-1, center, right, left)
    return left, center, right


if __name__ == '__main__':
    n = 5
    left = [1, 2, 3, 4, 5]
    center = []
    right = []
    left,  center, right = hanoi(n, left, right, center)
    print(left, center, right)