"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""


class Solution:

    def sortedSquares(self, A):
        for i in range(len(A)):
            A[i] = A[i] ** 2
        print(sorted(A))


def main():
    s = Solution()
    s.sortedSquares([-7, -3, 2, 3, 11])


if __name__ == '__main__':
    main()
