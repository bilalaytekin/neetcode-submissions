class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(
            c for c in s.lower() 
            if 'a' <= c <= 'z' or '0' <= c <= '9'
            )
        return t == t[::-1]