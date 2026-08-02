# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = collections.deque()
        q.append(root)
        # print(root.val)
        v = root.val
        while q:
            node = q.popleft()
            if node:
                v = max(v,node.val)
                if v <= node.val:
                    print(node.val)
                    count+=1
                q.append(node.left)
                q.append(node.right)
                
        return count
                