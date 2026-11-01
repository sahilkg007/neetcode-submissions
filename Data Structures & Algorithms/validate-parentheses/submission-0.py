class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen= {')': '(', '}':'{', ']':'['}
        stack = []
        for ch in s:
            if ch in closetoopen:
                print(ch,stack[-1])
                if not stack and ch != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)

        return True if not stack else False