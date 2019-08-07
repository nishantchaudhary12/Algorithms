#heap sort


def heapify(arr, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    if left <= n and arr[left] > arr[i]:
        largest = left
    else:
        largest = i
    if right <= n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)


def buildMaxHeap(arr, heapsize):
    # heapsize = len(arr)
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, i, heapsize)


def heapSort(arr):
    heapsize = len(arr) - 1
    buildMaxHeap(arr, heapsize)
    for i in range(heapsize, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapsize -= 1
        heapify(arr, 0, heapsize)


def main():
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heapSort(arr)
    print(arr)


main()