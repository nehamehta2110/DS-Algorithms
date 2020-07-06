"""
You have been given a positive integer N. You need to find and print the
Factorial of this number. The Factorial of a positive integer N refers to the product of
all number in the range from 1 to N.
"""


def fact(N):

    if N == 0 or N == 1:
        return N
    else:
        return fact(N - 1) * N


def main():
    N = int(input())
    print(fact(N))


if __name__ == "__main__":
    main()
