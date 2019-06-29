#merge sort

import sys


def merge(user_inp, start_index, mid, end_index):
    n1 = mid - start_index + 1
    n2 = end_index - start_index + 1
    list1 = user_inp[start_index:mid+1]
    list2 = user_inp[mid+1:end_index+1]
    list1.append(sys.maxsize)
    list2.append(sys.maxsize)
    i = 0
    j = 0
    for k in range(start_index, end_index+1):
        if list1[i] <= list2[j]:
            user_inp[k] = list1[i]
            i += 1
        else:
            user_inp[k] = list2[j]
            j += 1
    return user_inp


def merge_sort(user_inp, start_index, end_index):
    if start_index < end_index:
        mid = (start_index + end_index)//2
        merge_sort(user_inp, start_index, mid)
        merge_sort(user_inp, mid + 1, end_index)
        user_inp = merge(user_inp, start_index, mid, end_index)

    return user_inp


def main():
    user_inp = [5, 2, 4, 6, 1, 3]
    print('Sorted Output:', merge_sort(user_inp, 0, 5))


main()