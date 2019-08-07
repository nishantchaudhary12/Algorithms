#radix sort


def countinSort(arr, exp):
    output = [0] * len(arr)

    count = [0] * 10

    for each in arr:
        indx = each // exp
        count[indx % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        indx = arr[i] // exp
        output[count[indx % 10] - 1] = arr[i]
        count[indx % 10] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    length = max(arr)
    exp = 1

    while length//exp > 0:
        countinSort(arr, exp)
        exp *= 10


def main():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radixSort(arr)
    print(arr)
    

main()