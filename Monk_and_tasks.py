"""
To test Monk A, Monk D provided him tasks for N days in the form of an array Array,
where the elements of the array represent the number of tasks.
The number of tasks performed by Monk A on the ith day is the number of ones in the binary representation of Arrayi.
Monk A is fed up of Monk D, so to irritate him even more,
he decides to print the tasks provided in non-decreasing order of the tasks performed by him on each day. Help him out!
Input:
The first line of input contains an integer T, where T is the number of test cases.
The first line of each test case contains N, where N is the number of days.
The second line of each test case contains Array array having N elements, where Arrayi represents the number of tasks provided by Monk D to Monk A on ith day.
Output:
Print all the tasks provided to Monk A in the non-decreasing order of number of tasks performed by him.
"""


def check_work(num):
    count = 0
    while(num):
        num = num & (num-1)
        count += 1
    return count


def arrange(A, N):

    output = {}

    for i in range(N):
        output[A[i]] = check_work(int(A[i]))
    print(sorted(output.items(), key = lambda kv:(kv[1], kv[0])))


def main():
    T = int(input("enter T"))
    for i in range(T):
        N = int(input("enter N"))
        A = input("enter elements separated by space")
        A = A.strip().split()
        arrange(A, N)


if __name__ == '__main__':
    main()