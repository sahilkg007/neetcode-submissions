"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head

        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        curr = head
        while curr: 
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        newhead = head.next
        curr = head

        while curr:
            copy = curr.next
            curr.next = copy.next
            if l2.next:
                l2.next = l2.next.next
            curr = curr.next

        return newhead
            



            



