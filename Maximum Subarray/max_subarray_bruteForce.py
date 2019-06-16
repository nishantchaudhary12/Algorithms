#Brute force


def maximum_subarray(price_change):
    max_sum = 0
    for indx in range(len(price_change)):
        each = price_change[indx]
        pair_sum = 0
        j = indx + 1
        while j < (len(price_change) - 1):
            pair_sum += sum(price_change[indx:j+1])
            if pair_sum > max_sum:
                max_sum = pair_sum
                indx_list = [indx, j+1]

            pair_sum = 0
            j += 1
    print('Maximum Subarray Index:', indx_list)
    print(price_change[indx_list[0]:indx_list[1]])


if __name__ == '__main__':
    price_change = [-13, 3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    maximum_subarray(price_change)
