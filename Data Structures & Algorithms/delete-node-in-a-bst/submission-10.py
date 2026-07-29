# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self,root: TreeNode, key: int) -> TreeNode:
        cur = root
        parent = None

        # Step 1: Search for the node and track its parent
        while cur and cur.val != key:
            parent = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        # Node not found
        if not cur:
            return root

        # Step 2: Delete the node based on its children count
        if cur.left and cur.right:
            succ_parent = cur
            succ = cur.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            
            cur.val = succ.val
            cur = succ
            parent = succ_parent

        # Step 3:
        # at this point atmost one children
        child = cur.left if cur.left else cur.right
        if not parent:
            return child   # Deleting the root node itself

        if parent.left == cur:
            parent.left = child
        else:
            parent.right = child

        return root

