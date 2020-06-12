class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = []
        leng = len(needle)
        
        if len(needle) == 0:
            return 0
        
        for idx in range(len(haystack)-leng+1):
            if haystack[idx:idx+leng] == needle:
                print(idx, haystack[idx:idx+leng])
                return idx
            else:
                pass
        
        return -1
