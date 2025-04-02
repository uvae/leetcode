class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): return False

        s = str(x); l = len(s)
        for i in range(l):
            if s[i] != s[l-i-1]: return False
        
        return True