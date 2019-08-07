#quick sort


def quickSort(sample_input, low, high):
    if low < high:
        pivot = partition(sample_input, low, high)
        quickSort(sample_input, low, pivot - 1)
        quickSort(sample_input, pivot + 1, high)


def partition(sample_input, low, high):
    x = sample_input[high]
    i = low - 1
    for j in range(low, high):
        if sample_input[j] <= x:
            i = i + 1
            sample_input[j], sample_input[i] = sample_input[i], sample_input[j]
    sample_input[i + 1], sample_input[high] = x, sample_input[i+1]
    return i+1


def main():
    sample_input = [2, 6, 5, 3, 8, 7, 1, 0, 4]
    quickSort(sample_input, 0, len(sample_input) - 1)
    print(sample_input)


main()