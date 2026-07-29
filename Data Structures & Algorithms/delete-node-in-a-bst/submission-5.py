# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self,root: TreeNode, key: int) -> TreeNode:
        curr = root
        parent = None

        # Step 1: Search for the node and track its parent
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        # Node not found
        if not curr:
            return root

        # Step 2: Delete the node based on its children count

        # Case 1 & 2: Node has 0 or 1 child
        if not curr.left or not curr.right:
            # Determine the replacement child (could be None if leaf)
            child = curr.left if curr.left else curr.right

            # If target node is the root itself
            if not parent:
                return child

            # Link parent directly to the child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child

        # Case 3: Node has 2 children
        else:
            # Find in-order successor (smallest in right subtree) and its parent
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left

            # Copy successor's value to current node
            curr.val = succ.val

            # Unlink the successor (successor can only have a right child at most)
            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right

        return root