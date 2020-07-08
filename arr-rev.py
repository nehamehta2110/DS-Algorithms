def reverseArray(a):

    """
    Print all N integers in A in reverse order as a single line of space-separated integers.
    :param a: input array
    :return: reverse array
    """

    for i in a[::-1]:
        print(i, end=' ')


if __name__ == '__main__':

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    reverseArray(arr)