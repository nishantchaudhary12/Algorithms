#merge sort


import sys


def merge(arr, start, mid, end):
    left = list()
    right = list()
    for i in range(mid - start + 1):
        left.append(arr[start + i])
    for j in range(end - mid):
        right.append(arr[mid + j + 1])
    left.append(sys.maxsize)
    right.append(sys.maxsize)

    i = 0
    j = 0
    for k in range(start, end+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)


def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    mergeSort(arr, 0, len(arr)-1)
    print(arr)


main()