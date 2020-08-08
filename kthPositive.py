"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Find the kth positive integer that is missing from this array.
Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
"""


class Solution:
    def findKthPositive(self, arr, k):
        res = [i for i in range(1, len(arr) + k + 1) if i not in arr]
        return res[k - 1]


def main():
    arr = [2, 3, 4, 7, 11]
    k = 5

    solve = Solution()
    print(solve.findKthPositive(arr, k))


if __name__ == '__main__':
    main()
