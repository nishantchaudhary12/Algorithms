#selection sort


def selectionSort(sample_input):
    for i in range(len(sample_input) - 1, -1, -1):
        largest = sample_input[i]
        idx = i
        for j in range(0, i):
            if largest < sample_input[j]:
                largest = sample_input[j]
                idx = j
        sample_input[idx] = sample_input[i]
        sample_input[i] = largest
    print(sample_input)


def main():
    sample_input = [44, 31, 25, 9, 20, 46, 11, 32, 17, 35]
    selectionSort(sample_input)


main()