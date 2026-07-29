# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Helper function: deletes `root` and returns the new subtree root
        def helper(node):
            # Case 1 & 2: If one of the subtrees is missing, return the other
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Case 3: Both children exist.
            # Attach the entire right subtree to the rightmost leaf of the left subtree.
            right_child = node.right
            last_right = find_last_right(node.left)
            last_right.right = right_child

            return node.left

        def find_last_right(node):
            while node.right:
                node = node.right
            return node

        # If the root itself is the target
        if root.val == key:
            return helper(root)

        # Iterative search for the node whose child matches `key`
        cur = root
        while cur:
            if cur.val > key:
                if cur.left and cur.left.val == key:
                    cur.left = helper(cur.left)
                    break
                else:
                    cur = cur.left
            else:
                if cur.right and cur.right.val == key:
                    cur.right = helper(cur.right)
                    break
                else:
                    cur = cur.right

        return root