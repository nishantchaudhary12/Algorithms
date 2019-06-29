#insertion sort


def insertion_sort(user_inp):
    for each in range(1, len(user_inp)):
        i = each - 1
        key = user_inp[each]
        while i > -1 and user_inp[i] > key:
            user_inp[i+1] = user_inp[i]
            i -= 1
        user_inp[i+1] = key

    return user_inp


def main():
    user_inp = [5, 2, 4, 6, 1, 3]
    print('Sorted Output:' , insertion_sort(user_inp))


main()