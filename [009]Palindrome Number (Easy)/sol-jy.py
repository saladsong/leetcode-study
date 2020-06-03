class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        while len(s) > 0:
            if s[0] != s[-1]:
                return False
            s = s[1:-1]
            
        return True
