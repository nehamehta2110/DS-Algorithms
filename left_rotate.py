#!/bin/python3

def array_rotate(a, n, d):

    temp = []

    for i in range(d,n):
        temp.append(a[i])

    a1 = []

    for i in range(d):
        a1.append(a[i])

    print(temp + a1)


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    array_rotate(a, n, d)
