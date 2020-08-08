"""
Given a binary tree, return the inorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        stack, res = [], []
        current = root

        while True:
            if current:
                stack.append(current)
                current = current.left
            if len(stack) == 0:
                return res
            if current is None:
                node = stack.pop()
                res.append(node.val)
                current = node.right


def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solve = Solution()
    print(solve.inorderTraversal(root))


if __name__ == '__main__':
    main()
