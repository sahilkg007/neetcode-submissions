class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            str = s
            str = str.replace(s[i],'')
            i+=1

            if str==str[::-1]:
                return True
        return False