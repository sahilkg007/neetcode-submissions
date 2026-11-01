class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        top = 0
        res = 0
        for i in operations:
            if i == '+':
                new = int(top) + int(stack[-2])
                stack.append(new)
            elif i == 'C':
                if stack:
                    stack.pop()
            elif i == 'D':
                new = 2*int(top)
                stack.append(new)
            else:
                stack.append(i)
                top = int(stack[-1])
        
        for i in stack:
            res = res + int(i)

        return res

