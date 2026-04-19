class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for i in operations:
            if i == '+':
                new = int(stack[-1]) + int(stack[-2])
                stack.append(new)
            elif i == 'C':
                if stack:
                    stack.pop()
            elif i == 'D':
                new = 2*int(stack[-1])
                stack.append(new)
            else:
                stack.append(i)
        print(stack)
        
        for i in stack:
            res = res + int(i)

        return res

