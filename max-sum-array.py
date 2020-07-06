"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""


class Solution:
    def __init__(self):
        self.sum = []

    def findMaxConsecutiveOnes(self, nums):

        sum_count = 0
        for i in range(len(nums)-1):
            if nums[i] == 1:
                sum_count += nums[i]
                if nums[i+1] == 0:
                    break
        self.sum.append(sum_count)
        print("sum", self.sum)
        if nums[i+2:]:
            self.findMaxConsecutiveOnes(nums[i+2:])

        else:
            print(max(self.sum))


def main():
    solve = Solution()
    solve.findMaxConsecutiveOnes([1, 1, 0, 0, 1, 1, 1, 1])


if __name__ == '__main__':
    main()


