class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = { ')':'(', '}':'{', ']':'['}
        stack = []

        for i in s:
            if i in close_to_open:
                if not stack or close_to_open[i]!=stack.pop():
                    return False
                # else:
                #     stack.append(i)
            else:
                stack.append(i)
        
        return False if stack else True

