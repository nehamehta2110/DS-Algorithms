"""You have been given an array A of size N consisting of positive integers.
You need to find and print the product of all the number in this array Modulo 10^9 + 7 .

Input Format:
The first line contains a single integer N denoting the size of the array.
The next line contains N space separated integers denoting the elements of the array

Output Format:
Print a single integer denoting the product of all the elements of the array Modulo 10^9 + 7 ."""


def find_product(N, array):
    answer = 1
    mod = (10 ** 9) + 7

    for i in range(N):
        answer = (answer * array[i]) % mod

    print(answer)


def main():

    N = int(input())
    array = list(map(int, input().strip().split()))

    find_product(N, array)


if __name__ == "__main__":
    main()
