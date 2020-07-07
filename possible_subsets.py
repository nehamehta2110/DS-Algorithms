"""
Print all possible subsets of a set
example: {a,b}
=> {}, {a}, {b}, {a,b}
"""


def possibleSubsets(array, N):

    for i in range(1, 2**N):
        for j in range(N):
            if i & (1 << j):
                print(array[j], end= ",")

        print("")


def main():
    array = ['abc', 'def', 'ghi']
    N = len(array)
    possibleSubsets(array, N)


if __name__ == '__main__':
    main()