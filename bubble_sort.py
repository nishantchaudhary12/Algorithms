#bubble sort


def bubble_sort(user_inp):
    for each in range(0, len(user_inp) - 1):
        for elem in range(len(user_inp) - 1, each, -1):
            if user_inp[elem] < user_inp[elem - 1]:
                temp = user_inp[elem]
                user_inp[elem] = user_inp[elem - 1]
                user_inp[elem - 1] = temp
    return user_inp


def main():
    user_inp = [5, 2, 4, 6, 1, 3]
    print('Sorted Output:', bubble_sort(user_inp))


main()