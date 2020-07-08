#!/bin/python


def plusMinus(arr):
    """
    It should print out the ratio of positive, negative and zero items in the array,
    each on a separate line rounded to six decimals.
    :param arr:
    :return: 3 decimals representing of the fraction of positive numbers,
            negative numbers and zeros in the array compared to its size.
    """
    count_pos = 0.0
    count_neg = 0.0
    count_zer = 0.0
    total = float(len(arr))

    for i in arr:
        if i > 0:
            count_pos += 1.0
        elif i < 0:
            count_neg += 1.0
        elif i == 0:
            count_zer += 1.0

    print(round((count_pos / total), 6))
    print(round((count_neg / total), 6))
    print(round((count_zer / total), 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
