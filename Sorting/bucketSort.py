#bucket sort


def bucketSort(sample_input):
    maxValue = max(sample_input)
    result = [0 for each in range(maxValue + 1)]
    sortedList = list()
    for each in sample_input:
        if result[each] == 0:
            result[each] = 1
        else:
            result[each] += 1
    for i in range(len(result)):
        while result[i] != 0:
            sortedList.append(i)
            result[i] -= 1
    print(sortedList)



sample_input = [4, 3, 8, 4, 9, 2, 6]
bucketSort(sample_input)