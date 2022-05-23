# 문제) https://leetcode.com/problems/balanced-binary-tree/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def check(root):
        if not root:
            return

        left = check(root.left)
        right = check(root.rigth)

        if left == 1 or\
                right == -1 or\
                abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return check(root) != 1

