class Solution:
    def romanToInt(self, s: str) -> int:
        res, tmp = 0, 0
        for idx in range(len(s)):
            try:           
                if s[idx] == 'M':
                    res += 1000
                elif s[idx] == 'D':
                    res += 500
                elif s[idx] == 'C':
                    tmp = 100
                    if s[idx+1] in ['D', 'M']:
                        tmp = tmp*(-1)
                    res += tmp
                elif s[idx] == 'L':
                    res += 50
                elif s[idx] == 'X':
                    tmp = 10
                    if s[idx+1] in ['L', 'C']:
                        tmp = tmp*(-1)
                    res += tmp
                elif s[idx] == 'V':
                    res += 5
                else:
                    tmp = 1
                    if s[idx+1] in ['V', 'X']:
                        tmp = tmp*(-1)
                    res += tmp
            except IndexError:
                res += tmp
        
        return res
