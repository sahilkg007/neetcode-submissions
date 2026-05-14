class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.extend([a,b,a+b])
                print(stack)
            elif i == "D":
                x = (stack.pop())
                stack.extend([x,x*2])
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        print(stack)
        return sum(stack)