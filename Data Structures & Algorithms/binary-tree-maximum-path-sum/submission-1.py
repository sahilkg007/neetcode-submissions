# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfsSum(cur):
            if not cur:
                return None

            l = dfsSum(cur.left)
            r = dfsSum(cur.right)

            nonlocal res
            res = max(res,l + cur.val + r, 0)
            return cur.val + max(l , r)
        
        dfsSum(root)
        return res


