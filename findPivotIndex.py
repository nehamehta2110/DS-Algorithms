"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation: The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
"""


class Solution:
    def sum_compute(self, arr):
        s = 0
        for i in range(len(arr)):
            s += arr[i]

        return s

    def pivotIndex(self, nums):

        if len(nums) < 3:
            return -1

        if self.sum_compute(nums[1:]) == 0:
            return 0

        for i in range(1, len(nums) - 1):

            if self.sum_compute(nums[:i]) == self.sum_compute(nums[i + 1:]):
                return i

        if self.sum_compute(nums[:len(nums) - 1]) == 0:
            return len(nums) - 1

        return -1


def main():
    solve = Solution()
    print(solve.pivotIndex([-1, -1, -1, -1, 1, 1]))


if __name__ == '__main__':
    main()
