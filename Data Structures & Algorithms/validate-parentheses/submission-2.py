class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen= {')': '(', '}':'{', ']':'['}
        stack = []
        for ch in s:
            if ch in closetoopen:
                if stack and closetoopen[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False